from search import load_data, search
import sys

def build_context():
    embeddings, chunks = load_data()
    top_chunks = search(sys.argv[1], embeddings, chunks)

    for i, (score, chunk) in enumerate(top_chunks, start=1):
        print(f"[Quelle {i}: {chunk["doc"]}, Seite: {chunk["page"]}]")
        print(f"{chunk["text"]}")
        print()

if __name__ == "__main__":
    build_context()