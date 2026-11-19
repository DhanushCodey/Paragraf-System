from rank_bm25 import BM25Okapi as bm25
import pytest

@pytest.fixture
def sample_corpus():
    docs = [
        "python pytest unit testing guide",
        "bm25 ranking algorithm for search engines",
        "bm25 bm25 bm25 keyword stuffing example with bm25 repeated",
        "cooking pasta with tomato sauce and basil",
    ]

    tokenized_docs = [doc.lower().split() for doc in docs]
    return docs, bm25(tokenized_docs)

def test_releveant_doc_rank_first(sample_corpus):
    docs, bm25_tk = sample_corpus
    query = "search ranking algorithm".split()
    score = bm25_tk.get_scores(query=query)

    top_doc = docs[score.argmax()]
    assert top_doc == "bm25 ranking algorithm for search engines"