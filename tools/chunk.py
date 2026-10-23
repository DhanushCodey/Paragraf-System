from clean_lines import clean_lines as cl
from pathlib import Path


def chunking(path):
    file = cl(path)
    chunk = []
    chunk_id = 0
    for page_id, page in enumerate(file, start=1):
        words = page.split()
        for start in range(0,  len(words), 150):
            if (start + 200) > (len(words)):
                break
            piece = words[start:start + 200]
            text = " ".join(piece)
            chunk.append(
                {
                    "doc": Path(path).name,
                    "page": page_id,
                    "chunk_id": chunk_id,
                    "text": text
                }
            )
            chunk_id += 1

    return chunk


if __name__ == "__main__":
    path = sorted(Path("data/raw").glob("*.pdf"))
    all_chunk = []

    # for i, chunk in enumerate(all_chunk):
    #     ch


