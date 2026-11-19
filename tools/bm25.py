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
    dont_know = build_bm25(chunks)
    
    


