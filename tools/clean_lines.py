import pymupdf
from extract import ext
import sys
import io
import contextlib
import re


def clean_lines(pdf_path):
    noisey_lines = ext(pdf_path)

    for i, line in enumerate(noisey_lines):
        line = re.sub(r"\xad\ns*", "", line)
        noisey_lines[i] = line

    
    return noisey_lines

if __name__ == "__main__":
    path = sys.argv[1]
    clean_lines(path)