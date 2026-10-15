from pathlib import Path
from clean_lines import clean_lines as cl


def process():

    Path("data/processed").mkdir(parents=True, exist_ok=True)
    pdf_files = Path("data/raw").glob("*.pdf")

    docs = {}
    msgs = []

    for file in pdf_files:
        name = file.name
        docs[name] = cl(file)

    for key, value in docs.items():
        op = Path("data/processed") / (Path(key).with_suffix(".txt"))

        with op.open("w", encoding="utf-8") as f:
            for pg_num, pg in enumerate(value, start=1):
                f.write(f"=== PAGE : {pg_num} ===\n")
                f.write(pg + "\n")

        saved_msg = f"Saved {f.name} : {len(value)} pages"
        msgs.append(saved_msg)

    for msg in msgs:
        print(msg)


if __name__ == "__main__":
    process()
