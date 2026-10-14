import pymupdf
from extract import ext
import sys
import io
import contextlib
import re


def clean_lines():
    pdf_path = sys.argv[1]
    noisey_lines = ext(pdf_path)

    for i, line in enumerate(noisey_lines):
        line = re.sub(r"\xad\ns*", "", line)
        noisey_lines[i] = line

    for line in noisey_lines:
        print(line)

if __name__ == "__main__":
    clean_lines()