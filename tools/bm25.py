import json
import re 
import numpy as np
from rank_bm25 import BM25Okapi as bm25api

# pipline
# 336 chunks -> tokenize each -> count words -> index

def load_chunks():
    file = "data/JSON/chunk.jsonl"
    chunks = []
    with open(file, encoding="utf-8") as data_sets:
        for ds in data_sets:
            chunks.append(json.loads(ds))
    
    return chunks

def tokenize(text):
    return re.findall(r"\w+", text.lower())

def build_bm25(chunks):
    tokenize_text = [tokenize(c['text']) for c in chunks]
    return bm25api(tokenize_text)

def search(question, bm25, chunks, k=5):
    score = bm25.get_scores(tokenize(question))

    top = np.argsort()[::-1][:k]
    result = []

    for i in top:
        result.append((score[i], chunks[i]))
    
    return result

if __name__ == "__main__":

    chunks = load_chunks()
    bm25 = build_bm25(chunks)

    tests = [
        ("Wie viele Soldatinnen und Soldaten dürfen bei der deutschen Beteiligung an UNMISS insgesamt eingesetzt werden?", "50"),
        ("Welche Geräte soll das BSI laut Entschließung des Innenausschusses bei der Marktüberwachung vorrangig prüfen?", "Router"),
        ("Welche Fraktion stimmte im Innenausschuss gegen den Gesetzentwurf zur Cyberresilienz-Verordnung?", "AfD"),
        ("Welche berufsständischen Organisationen für Pflegekräfte sollen laut Antrag auf Drucksache 21/1549 abgeschafft werden?", "Pflegekammern"),
    ] 
    
    for question, expected in tests:
        result = search(question, bm25, chunks)
        context = " ".join(chunk['text'] for score, chunk in result)
        found = expected.lower() in context.lower()

        print(f"\n=== {question}")
        print(f"Answer '{expected}' in top 5: {found}")
        for score, chunk in results:
            print(f"  {score:.2f} | {chunk['doc']} | page {chunk['page']}")




    
    


