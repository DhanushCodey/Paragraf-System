from search import load_data, search
import sys

def data():
    embeddings, chunks = load_data()
    result = search(sys.argv[1], embeddings, chunks)
    return result

def build_context(result):
    parts = []
    for i, (score, chunk) in enumerate(result, start=1):
        parts.append(f"[Quelle {i}: {chunk["doc"]}, Seite: {chunk["page"]}]\n{chunk["text"]}")
    
    return "\n\n".join(parts)

if __name__ == "__main__":
    result = data()
    context = build_context(result)

    print(context)