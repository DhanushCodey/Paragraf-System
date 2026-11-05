from clean_lines import clean_lines as cl
from pathlib import Path
import json


def chunking(path):

    file = cl(path)
    chunk = []

    for page_id, page in enumerate(file, start=1):
        words = page.split()
        for start in range(0,  len(words), 150):
            piece = words[start:start + 200]
            text = " ".join(piece)
            chunk.append(
                {
                    "doc": Path(path).name,
                    "page": page_id,
                    "chunk_id": 0,
                    "text": text
                }
            )

            if (start + 200) >= (len(words)):
                break

    return chunk


if __name__ == "__main__":
    Path("data/JSON").mkdir(parents=True, exist_ok=True)
    paths = sorted(Path("data/raw").glob("*.pdf"))
    all_chunk = []

    for file in paths:
        all_chunk.extend(chunking(file))

    for i, chunk in enumerate(all_chunk):
        chunk["chunk_id"] = i

    with open("data/JSON/chunk.jsonl", "w", encoding="utf-8") as f:
        for chunk in all_chunk:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    print(f"Total chunks : {len(all_chunk)}")
