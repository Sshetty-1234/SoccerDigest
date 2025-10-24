# summarize.py

import os
import datetime
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from . import Combine
from dotenv import load_dotenv

load_dotenv()



def run():
    """
    Generates the summary and returns it as a string.
    
    Parameters:
        groq_api_key (str): Optional. Your Groq API key. If not provided, will read from environment variable 'GROQ_API_KEY'.
    """
    try:
        # 1. Create PDF
        Combine.create_pdf(Combine.adp_info, Combine.goal_info, Combine.transfermarket_info)
    except Exception as e:
        return f"ERROR: PDF creation failed: {e}"

    current_date_str = datetime.date.today().strftime('%Y-%m-%d')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'data', 'full_report', f'Report_{current_date_str}.pdf')

    try:
        # 2. Load and split PDF
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        if not docs:
            return f"ERROR: No documents loaded from PDF: {file_path}"

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        if not splits:
            return "ERROR: No text splits generated from PDF."

        # 3. Embeddings and vectorstore
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
        retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        # 4. Initialize Groq chat model
        chat = ChatGroq(model="llama-3.1-8b-instant", api_key=os.getenv("GROQ_API_KEY"))
        FIXED_PROMPT = (
            "You are a friendly football pundit whose name is Soccer Buddy. "
            "Your purpose is to give a robust summary of the article provided"
        )

        # 5. RAG chain
        retrieved_docs = retriever.invoke("Can you please summarize this text")
        formatted_context = format_docs(retrieved_docs)
        full_prompt = f"{FIXED_PROMPT}\n\nContext:\n{formatted_context}\n\nQuestion: Can you please summarize this text"
        result = chat.invoke(full_prompt)
        content = result.content

        # Save to content.txt
        output_file_path = os.path.join(script_dir, 'data', 'summary', 'content.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return content

    except Exception as e:
        fallback_path = os.path.join(script_dir, 'data', 'summary', 'content.txt')
        with open(fallback_path, 'w', encoding='utf-8') as f:
            f.write("ERROR: The summary could not be generated during deployment. Check logs.")
        return f"ERROR: RAG execution failed: {e}"
