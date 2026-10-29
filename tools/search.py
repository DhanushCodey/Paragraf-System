from sentence_transformers import SentenceTransformer
import json,numpy as np
import pathlib as PATH

model = SentenceTransformer("intfloat/multilingual-e5-small")

# Retrival in RAG goal is to find the most convincing chunk that solves the user question.

def search_the_chunk():

    embeddings = np.load("data/embeddings/embedding.npy")
    chunks = []

    with open("data/JSON/chunk.jsonl", "r", encoding="utf-8") as file:
        for line in file:
            chunks.append(json.loads(line))

    return chunks


if __name__ == "__main__":
    json_file = search_the_chunk()

    print(json_file)
