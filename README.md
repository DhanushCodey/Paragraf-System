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



## Setup

```bash
git clone git@github.com:DhanushCodey/Paragraf-System.git
cd Paragraf-System
python3 -m venv .venv
# Mac: source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Data

The PDFs are not included in this repository. Download publicly available
Bundestag documents (Drucksachen) and place them in `data/raw/`.

try these websites:

https://dip.bundestag.de/suche?f.wahlperiode=21&f.typ=Dokument&f.herausgeber_dokumentart=Bundestag-Drucksache&rows=25&sort=verteildatum_ab

## Pipeline

| Step | Command | Output |
|---|---|---|
| 1. Extract text from one PDF | `python tools/extract.py data/raw/<file>.pdf` | printed to terminal |
| 2. Clean one PDF | `python tools/clean_lines.py data/raw/<file>.pdf` | printed to terminal |
| 3. Process all PDFs | `python tools/process_all.py` | `data/processed/*.txt` |
| 4. Find frequent noise lines | `python tools/feature_occ.py` | top 40 repeated lines |
| 5. Chunk all documents | `python tools/chunk.py` | `data/JSON/chunk.jsonl` |
| 6. Create embeddings | `python tools/embed.py data/JSON/chunk.jsonl` | `data/embeddings/embedding.npy` |

## Tests

```bash
python -m pytest tests/ -q
```

The first run downloads the embedding model
(`intfloat/multilingual-e5-small`) from Hugging Face.