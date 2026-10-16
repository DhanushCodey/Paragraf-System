from collections import Counter
from pathlib import Path

def noise_reduction():
    paths = Path("data/processed").glob("*.txt")
    # paths = [Path("data/processed/2106512.txt")]
    counts = Counter()

    for file in paths:
        lines= file.read_text(encoding="utf-8").splitlines()
        good_lines = []

        for line in lines:
            line = line.strip()

            if line.startswith("=== PAGE") or not line:
                continue
            else :
                good_lines.append(line)
        
        counts.update(good_lines)

    for line, num in counts.most_common(40):
            print(f"{line} : {num}")

if __name__ == "__main__":
    noise_reduction()