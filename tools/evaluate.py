import csv
from search import load_data, search
from answer import data, ask_llm, build_context

embeddings, chunks = load_data()


def read_eval():

    retrieval_hits = 0
    retrieval_total = 0
    answer_hits = 0

    all_result = []
    by_type = {}

    with open("eval/questions.csv", "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))


    for row in rows:
        result = search(row['question'], embeddings, chunks)
        found_docs = [chunk["doc"] for score, chunk in result]

        if row["doc"]:
            retrieval_ok = row["doc"] in found_docs
        else :
            retrieval_ok = None
        
        context = build_context(result)
        answer = ask_llm(row["question"], context)
        answer_ok = row["expected"].lower() in answer.lower()
        
        t = row["type"]
        if t not in by_type:
            by_type[t] = [0,0]
        by_type[t][1] += 1
        if answer_ok:
            by_type[t][0] += 1 

        if retrieval_ok is not None:
            retrieval_total += 1
            if retrieval_ok:
                retrieval_hits += 1
        if answer_ok:
            answer_hits += 1

        all_result.append(
            {
                "id": row["id"], 
                "type": row["type"], 
                "retrieval_ok": retrieval_ok, 
                "answer_ok": answer_ok, 
                "answer": answer
            }
        )

        print(f"[{row['id']}] type: {row['type']:8} retrieval: {retrieval_ok} | answer: {answer_ok} | expected: {row['expected']}")

    print()
    for t, (correct, total) in by_type.items():
        print(f"{t:8} {correct}/{total}")

    with open ("eval/result.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "type","retrieval_ok","answer_ok","answer"]) 
        writer.writeheader()
        writer.writerows(all_result)
                
            
    total = len(rows)
    print(f"\nRetrieval: {retrieval_hits}/{retrieval_total}")
    print(f"Answers:   {answer_hits}/{total}")

if __name__ == "__main__":
    read_eval()
