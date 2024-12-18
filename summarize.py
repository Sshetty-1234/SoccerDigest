from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from NewScaper.Combine import 




# Loading up the documents
loader = PyPDFLoader("data/Report_2024-10-31.pdf")  # Load your PDF file
data = loader.load()

# Need to chunk the text up
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=1000)
docs = text_splitter.split_documents(data)

# Need to take the respective chunks and make text representaions
# I am also using the google gemini to make my questions
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY"))

# Now store your chunks and their embeddings in a VectorDB

vectorstoredb = Chroma.from_documents(documents=docs, embedding=embeddings)
retriever = vectorstoredb.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Testing to see if the retreiwing works
# I am basically checking if based on a semantic query do I get the relevant stuff
retrieved_docs = retriever.invoke("Who is Ryan Tolmich")

# For testing purposes to see what the output is like
# print(retrieved_docs[0].page_content)

# Now to use the actualy llm to make the question answering
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

system_prompt = (
   "You a soccer pundit"
    "\n\n"
    "{context}"
)

# Set up the prompt for the QA chain
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

# Create the RAG chain
chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, chain)

response = rag_chain.invoke({"input": "What is this article about"})
print((response["answer"]))
