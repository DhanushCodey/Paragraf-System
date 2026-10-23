from extract import ext
import sys
import re

NOISE_PATTERNS = [
    r"Deutscher Bundestag – \d+\. Wahlperiode",
    r"Vorabfassung – wird durch die lektorierte Fassung ersetzt\.",
    r"Drucksache \d+/\d+",
    r"– \d+ –",
    r"Deutscher Bundestag",
    r"\d+\. Wahlperiode",
]

def remove_noise(page):
    kept = []
    for line in page.splitlines():
        is_noise = False
        for pattern in NOISE_PATTERNS:
            if re.fullmatch(pattern, line.strip()):
                is_noise = True
        if not is_noise:
            kept.append(line)

    return "\n".join(kept)


def clean_lines(pdf_path):
    file = ext(pdf_path)

    for i, page in enumerate(file):
        text = re.sub(r"\xad\s*", "", page)
        text = remove_noise(text)
        file[i] = text

    return file


if __name__ == "__main__":
    path = sys.argv[1]
    file = clean_lines(path)
    
    for page in file:
        print(page)
