# Paragraf-System

PURPOSE : The Bundestag published many big docx, and it hard for internatioanl students like me to get a gasp of with a minimal knowledge of german. So the RAG:Paragraf sys that, I build finds the answer and summarizes it, its a helper where user can ask Q:in english and sys gives A:in english while searching the German:Deutsch documents.

RAG -> Retrival Augmented Generation

Retrival : Searching the exact chunk that matches the user question.
Augmented : Adding those chunks in prmpt as the background context.
Generation : passing the asnwer and questioning the llm.

RAG-Pipline
- Data Prep
- Chunking / Segmentation
- Embedding / Vector Embeddings / making them into numbers
- Storage

PyMuPDF : is a highly efficient Python library used for extracting, analyzing, rendering, and manipulating PDFs and other document formats.

nano .gitignore
- .venv/
- data/raw/
: telling git to ignore these file.

extract.py 

    - extract the pages and text in a list format.

clean_lines.py

    - using claude i find most occuring noise patter in the pdf i upload. <manually>
  
    - > remove_noise(page)
      - give the page :
        1. it takes the pattern-line using re.fullmatch(patter, string, flags=0) : return if the match obj if only the str matches the conition.
        2. so basically it checks the entire line consist only the patter if yes : true else : false
        3. if yes ignore if no : add the line to the list and return the line with "\n"

    -> clean_line(pdf_path):
       - gives path to the extract() and get's the list
       - now it take away the "\xad\" using re.sub(r"\xad\*s", "", page) -> so basically turns the str(\xad\) into empty
       - and calls the remove_noise(page) for noise check
       - and return the list:file

process_all.py

    - process()
      - creates a data/processed directory and it its available then ignore.
      - creates a obj of .pdf files in a list
      - creates empty docs = {}:dict -> store all the file name as key:str and their data as a values:list
      - creates empty msg = []:list -> stores the total file_names and the length of the pages to tell its completed succesfully
       
      1. opens the dict
      2. creates a .txt file
      3. opens the .txt file
      4. writes a new line PAGE {pg_no}=== 
      5. adds the str from the value to the .txt. file in loop
      6. return the msg

feature_occ.py
    - takes in all the .txt paths
    - gets the file in the paths
    - reads the file line using .read_text()
    - ignore the "=== pages ===" in the .txt using .startswith()
    - store the strings in good_line list:[]
    - and store the entire list in the Counter() -> collection
        -  basically counts how the words ocurrence. in a dict data_type
   - return the keys:words and values:counts

<------------------DATA PREPARATION ENDS HERE----------------------------------->

<-----------------------CHUNKING------------------------------------------------>
The next step in building a RAG-Model
Chunking : Beaking down the larger text into smaller bit text, so an AI can understand it easily.

chunk.py
    
    - chunking()
        - takes the files and passes it to the clean_lines.py/clean_line(path)
        - creates a empty-list chunk[] : list of dict
        - loops the processed file with idx and page
        - splits the pages into text or words using .split() = words
        - now loops the start index with skip_value of 150 because over lap can be 50 words
          - (0, 200), (150, 350), (300, 500).....<overlap is 50 words>
        - next the piece = [start:start+200] where it stores the text from 0 to 200 and then 150 to 350
        - store those chunk_words in text with a space of using " ".join(piece)
          - simple words we split the words using .split() now making again this a sentence using " ".join(...)
        - store this in the chunk list in from of dict with values
          - doc : path_name
          - page_id : page_number using loop
          - chunk_id : looping the dicts
          - chunk : the unsplited final chunk

    - main()
      - create a folder of data/JSON if it exist ignores
      - passes all the .pdf files to chunk.py
      - creates a empty list all_chunk[]
      - then loops all the file to chunking() and store it in the all_chunks() using .extend()
      - creats the file unique chunk_id by looping all_chunk
      - then opens the .json file and dumps all_chunks into the .json file using .dump()
        - f.write(json.dumps(chunk, ensure_ascii=False), "\n") 
          - ensure_ascii=False -> python keeps all the spl char
          - "/n" -> to paste dict in a new line
      - pints the total_length of the all_chunks list

<--------------------------EMBEDDING------------------------------------------------>

