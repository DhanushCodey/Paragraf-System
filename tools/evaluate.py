import csv
from search import load_data, search
from answer import data, ask_llm, build_context

embeddings, chunks = load_data()


def read():
    result = []
    found_docs = []

    with open("eval/questions.csv", "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        result.append(search(row['question'], embeddings, chunks))

    for score, chunk in result:
        found_docs.append(chunk["docs"])


if __name__ == "__main__":
    read()
