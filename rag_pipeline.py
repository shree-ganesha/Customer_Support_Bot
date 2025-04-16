import json
import os
import requests
from langchain.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GOOGLE_API_KEY}"


def get_retriever():
    embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
    
    )
    db = Chroma(
    persist_directory=r"D:\Tryouts\task\chroma_db",
    embedding_function=embedding
    )
    retriever = db.as_retriever(search_kwargs={"k": 5})
    return retriever

def get_answer(question, retriever):
    results = retriever.get_relevant_documents(question)
    context = "\n\n".join([doc.page_content for doc in results])
    headers = {
    "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"You must answer questions using only the context provided. "
                            f"If the answer is not in the context, say 'I don't know.'\n\n"
                            f"If user greets or say bye just greet or end conversation accordingly."
                            f"Do not give short answer give explained answer always."
                            f"Context: {context}\n\nQuestion: {question}"}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"].strip()