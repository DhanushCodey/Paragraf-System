import pymupdf
import sys

def ext(pdf_path):
    doc = pymupdf.open(pdf_path)

    # for page_num, page in enumerate(doc, start=1):
    #     page_text = page.get_text()
        # lines = page_text.splitlines() -> create these lines in pdf as list of ..line[.line1.,.line2.,.line3.]

        # print("oderder" in page_text )
        # print(repr(page_text))

    pages = []
    for page in doc:
        pages.append(page.get_text())
        
    return pages
        
if __name__ == "__main__":

    try :
        if len(sys.argv) < 2 :
            print("Usage : tools/extract.py <path:missing>")
            sys.exit(1)
        txt = ext(sys.argv[1])
        for page_num , page in enumerate(txt, start=1):
            print(page)
            print("-"*100)
            print(page_num)
            print("-"*100)
            
    except FileNotFoundError as e :
        print(f"Path error: {e}")
    