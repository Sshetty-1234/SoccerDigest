from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
import os

# Load PDF
loader = PyPDFLoader("Report_2024-12-17.pdf")
docs = loader.load()

# Split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)
splits = text_splitter.split_documents(docs)

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


prompt_template = """You are a friendly football pundit whose name is Soccer Buddy.
Your purpose is to give a robust summary of the following article:

{text}

Question: {question}"""
prompt = ChatPromptTemplate.from_template(prompt_template)

# Store in Chroma vector database
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

# Create retriever
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Format retrieved docs
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Initialize Groq chat model
chat = ChatGroq(model="llama-3.1-8b-instant")
FIXED_PROMPT = "You are a friendly football pundit whose name is Soccer Buddy. Your purpose is to give a robust summary of the article provided"

# Define RAG chain
def rag_chain(question):
    retrieved_docs = retriever.invoke(question)
    formatted_context = format_docs(retrieved_docs)
    prompt = f"Question: {question}\n\nContext: {formatted_context}"
    full_prompt = f"{FIXED_PROMPT}\n\nContext:\n{formatted_context}\n\nQuestion: {question}"
    return chat.invoke(full_prompt)
    

# Run example
result = rag_chain("Can you please summarize this text")
print(result.content)

