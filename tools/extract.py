import pymupdf
import sys

def ext(pdf_path):
    doc = pymupdf.open(pdf_path)

    for page_num, page in enumerate(doc, start=1):
        page_text = page.get_text()
        # lines = page_text.splitlines() -> create these lines in pdf as list of ..line[.line1.,.line2.,.line3.]

        print(page_text)
        
        print("-"*100)
        print(f"PAGE NUM : {page_num}")
        print("-"*100)

if __name__ == "__main__":

    try :
        if len(sys.argv) < 2 :
            print("Usage : tools/extract.py <path:missing>")
            sys.exit(1)
        ext(sys.argv[1])
    except FileNotFoundError as e :
        print(f"Path error: {e}")
    