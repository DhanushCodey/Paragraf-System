from search import load_data, search
import sys
import ollama as llm

SYSTEM_PROMPT = """Du bist ein Assistent für Dokumente des Deutschen Bundestages.
Beantworte die Frage NUR mit Informationen aus den gegebenen Quellen.
Nenne nach jeder Aussage die Quelle, z. B. (Quelle 2).
Wenn die Antwort nicht in den Quellen steht, antworte genau:
"Diese Information steht nicht in den Dokumenten."
Antworte kurz und sachlich."""

def data(question):
    embeddings, chunks = load_data()
    result = search(question, embeddings, chunks)
    return result

def build_context(result):
    parts = []
    for i, (score, chunk) in enumerate(result, start=1):
        parts.append(f"[Quelle {i}: {chunk["doc"]}, Seite: {chunk["page"]}]\n{chunk["text"]}")
    
    return "\n\n".join(parts)

def ask_llm(question, context):

    response = llm.chat(
        model= "qwen2.5:3b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Quellen:\n{context}\n\nFrage: {question}"},
        ],
        options= {"temperature": 0},
    )

    return response["message"]["content"]
    

if __name__ == "__main__":
    question = sys.argv[1]
    result = data(question)
    context = build_context(result)
    answer = ask_llm(question, context)

    print("Antwort: ", answer)
    print("\nQuellen:")
    for i, (score, chunk) in enumerate(result, start=1):
        print(f"[{i}] {chunk['doc']}, Seite {chunk['page']} (Score {score:.3f})")


