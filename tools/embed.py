from sentence_transformers import SentenceTransformer, util
import json, sys, numpy as np
from pathlib import Path

model = SentenceTransformer("intfloat/multilingual-e5-small")


def embeddings(path):
    chunks = []
    with open(Path(path), encoding="utf-8") as file :
        for line in file:
            chunks.append(json.loads(line))
    
    text = ["passage : " + c["text"] for c in chunks]

    embeddings = model.encode(text, normalize_embeddings=True, show_progress_bar=True)
    
    return embeddings

if __name__ == "__main__":
    Path("data/embeddings").mkdir(parents=True, exist_ok=True)
    path = Path(sys.argv[1])
    vector = embeddings(path)

    np.save("data/embeddings/embedding.npy", vector)
    
