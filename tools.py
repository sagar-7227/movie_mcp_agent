import os

from dotenv import load_dotenv
from pymongo import MongoClient
from google import genai

load_dotenv()

# ==========================
# MongoDB
# ==========================

mongo_client = MongoClient(
    os.getenv("MDB_MCP_CONNECTION_STRING")
)

db = mongo_client["sample_mflix"]

embedded_movies = db["embedded_movies"]

# ==========================
# Gemini
# ==========================

genai_client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# ==========================
# Embedding Generator
# ==========================

def generate_embedding(text: str):

    response = genai_client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config={
            "output_dimensionality": 1536
        }
    )

    if not response.embeddings:
        raise RuntimeError(
            "No embeddings returned."
        )

    embedding = response.embeddings[0].values

    if embedding is None:
        raise RuntimeError(
            "Embedding values missing."
        )

    return embedding

# ==========================
# Semantic Search
# ==========================

def search_movies(query: str):

    query_vector = generate_embedding(query)

    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "path": "plot_embedding",
                "queryVector": query_vector,
                "numCandidates": 150,
                "limit": 5
            }
        },
        {
            "$project": {
                "_id": 0,
                "title": 1,
                "year": 1,
                "directors": 1,
                "plot": 1,
                "score": {
                    "$meta": "vectorSearchScore"
                }
            }
        }
    ]

    return list(
        embedded_movies.aggregate(pipeline)
    )