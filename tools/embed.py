from sentence_transformers import SentenceTransformer, util
import json
import sys
import numpy as np
from pathlib import Path

model = SentenceTransformer("intfloat/multilingual-e5-small")


def embeddings(path):
    chunks = []
    with open(Path(path), encoding="utf-8") as file:
        for line in file:
            chunks.append(json.loads(line))

    text = ["passage : " + c["text"] for c in chunks]

    embeddings = model.encode(
        text, normalize_embeddings=True, show_progress_bar=True)

    return embeddings


if __name__ == "__main__":
    Path("data/embeddings").mkdir(parents=True, exist_ok=True)
    if (len(sys.argv) < 2):
        print("python tools/embed.py {NEED PATH}")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        raise FileNotFoundError(f"The specified path {path} does not exist")
    else:
        vector = embeddings(path)
        np.save("data/embeddings/embedding.npy", vector)
