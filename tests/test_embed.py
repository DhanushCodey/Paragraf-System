from sentence_transformers import SentenceTransformer, util
import pytest

model = SentenceTransformer("intfloat/multilingual-e5-small")

# HF_HUB_OFFLINE=1 python -m pytest tests/test_embed.py -q
                                  # tests/test_embed.py::test_embedding_shape (-q || <empty>)

@pytest.fixture(scope="module")
def test_sentence():
    sentences = [
        "query: Wer ist für die Marktüberwachung digitaler Produkte zuständig?",
        "passage: Das BSI ist die zuständige Marktüberwachungsbehörde für Produkte mit digitalen Elementen.",
        "passage: Die NATO-Versammlung trifft sich zweimal im Jahr.",
    ]
    
    embeddings = model.encode(sentences)
    return embeddings

def test_embedding_shape(test_sentence):

    expected = (3, 384)
    
    assert expected == test_sentence.shape

def test_cosine_similarity(test_sentence):
    embeddings = test_sentence

    cos_sim = util.cos_sim(embeddings, embeddings)

    assert cos_sim[0][1] >= cos_sim[0][2]

