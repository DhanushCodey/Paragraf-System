from sentence_transformers import SentenceTransformer
import json,numpy as np
import pathlib as PATH
import sys

model = SentenceTransformer("intfloat/multilingual-e5-small")

# Retrival in RAG goal is to find the most convincing chunks that solves the user question.

def load_data():

    embeddings = np.load("data/embeddings/embedding.npy")
    chunks = []

    with open("data/JSON/chunk.jsonl", "r", encoding="utf-8") as file:
        for line in file:
            chunks.append(json.loads(line))

    return embeddings ,chunks

def search(question ,embeddings, chunks, k = 5):
    q_vec = model.encode("query: " + question, normalize_embeddings=True)
    score = embeddings @ q_vec

    top = np.argsort(score)[::-1][:k]
    result = []

    for i in top:
        result.append((score[i], chunks[i]))
    
    return result

if __name__ == "__main__":
    embeddings, chunks = load_data()
    result = search(sys.argv[1], embeddings, chunks)

    for score, chunks in result:
        print(f"{score:.3f} | {chunks["doc"]} | page {chunks["page"]}")
        print(chunks["text"][:200])
        print("-" * 60)
