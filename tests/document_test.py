import pytest

from personalized_information_flow.clustering.document import Document


@pytest.mark.parametrize(
    "text,exp_words",
    [
        ["", []],
        ["Test text", ["test", "text"]],
        ["TESTTEXT", ["testtext"]],
        ['"TESTTEXT"', ["testtext"]],
        ['"TESTTEXT". Another text.', ["testtext", "another", "text"]],
        ["'test', 'test2'", ["test", "test2"]],
        ["test - test2", ["test", "test2"]],
    ],
)
def test_document_get_words(text, exp_words):
    document = Document(text)
    words = document.get_words()
    assert words == exp_words


@pytest.mark.parametrize(
    "text,exp_words",
    [
        ["", []],
        ["Test text", ["test", "text"]],
        ["Test text text TeST", []],
    ],
)
def test_document_get_unique_words(text, exp_words):
    document = Document(text)
    words = document.get_unique_words()
    assert words == exp_words


@pytest.mark.parametrize(
    "text,exp_ngrams",
    [
        ["", []],
        ["Test text", [["test", "text"]]],
        ["test1 test2 test3 test4", [["test1", "test2"], ["test2", "test3"], ["test3", "test4"]]],
    ],
)
def test_document_bigrams(text, exp_ngrams):
    document = Document(text)
    ngrams = document.get_ngrams()
    assert ngrams == exp_ngrams
