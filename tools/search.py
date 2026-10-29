from sentence_transformers import SentenceTransformer
import json,numpy as np
import pathlib as PATH

model = SentenceTransformer("intfloat/multilingual-e5-small")

# Retrival in RAG goal is to find the most convincing chunk that solves the user question.

def load_data():

    embeddings = np.load("data/embeddings/embedding.npy")
    chunks = []

    with open("data/JSON/chunk.jsonl", "r", encoding="utf-8") as file:
        for line in file:
            chunks.append(json.loads(line))

    return embeddings ,chunks

def search(question ,embeddings, chunk, k = 5):
    n_que = model.encode("query: " + question, normalize_embeddings=True)

    return n_que


if __name__ == "__main__":
    pass
