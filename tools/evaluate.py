import csv
from search import load_data, search
from answer import data, ask_llm, build_context

embeddings, chunks = load_data()


def read_eval():

    retrieval_hits = 0
    retrieval_total = 0
    answer_hits = 0
    rows = []

    with open("eval/questions.csv", "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))


    for row in rows[:5]:
        result = search(row['question'], embeddings, chunks)
        found_docs = [chunk["doc"] for score, chunk in result]

        if row["doc"]:
            retrieval_ok = row["doc"] in found_docs
        else :
            retrieval_ok = None
        
        context = build_context(result)
        answer = ask_llm(row["question"], context)
        answer_ok = row["expected"].lower() in answer.lower()

        if retrieval_ok is not None:
            retrieval_total += 1
            if retrieval_ok:
                retrieval_hits += 1
        if answer_ok:
            answer_hits += 1

        print(f"[{row['id']}] type: {row['type']:8} retrieval: {retrieval_ok} | answer: {answer_ok} | expected: {row['expected']}")

    total = len(rows[:5])
    print(f"\nRetrieval: {retrieval_hits}/{retrieval_total}")
    print(f"Answers:   {answer_hits}/{total}")

if __name__ == "__main__":
    read_eval()
