⚽ Soccer Digest

Soccer Digest is a Django-based web application that provides up-to-date information about Premier League teams, player squads, and live rankings. It combines a traditional relational database with cutting-edge Retrieval-Augmented Generation (RAG) techniques to deliver insightful, AI-generated summaries of current soccer events.

🚀 Features

Team & Squad Database

Stores squad information for all Premier League teams in a local SQLite database.

Enables users to view and query team compositions, player details, and positions.

Dynamic API Integration

Pulls real-time match and ranking data from a live football API.

Displays current standings, fixtures, and game outcomes dynamically.

Soccer Buddy (RAG Module)

The core feature of Soccer Digest.

Runs daily web scrapes from popular football news and analytics sites.

Uses LangChain and LLMs to summarize and compile soccer insights.

Employs retrieval-augmented generation (RAG) for contextual, fact-grounded responses.

🧠 Tech Stack

Backend: Django (Python)
Frontend: HTML, CSS
Database: SQLite
AI & Data Pipeline:

langchain_community for document loading and vector storage

langchain_text_splitters for text chunking

langchain_huggingface for embedding generation

langchain_groq for LLM integration

Chroma as the vector store backend

datetime for scheduling daily scrapes

⚙️ Installation

Clone the repository

git clone https://github.com/yourusername/soccer-digest.git
cd soccer-digest


Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Start the development server

python manage.py runserver


Visit http://127.0.0.1:8000/ to view the app.

🧩 Example Workflow (Soccer Buddy)

Web scraper collects daily soccer data (e.g., match reports, analytics).

Data is processed and split using RecursiveCharacterTextSplitter.

Text embeddings are generated using HuggingFaceEmbeddings.

Chroma stores embeddings for semantic retrieval.

Queries are passed through ChatGroq, producing RAG-based summarie
