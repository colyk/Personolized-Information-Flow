from collections import Counter
import re


class Document:
    def __init__(self, text: str, tags: list[str] = None) -> None:
        self.text = text

    def get_words(self) -> list[str]:
        text = self.text.lower()
        text = self._remove_pronounciation(text)
        return text.split()

    def _remove_pronounciation(self, text: str) -> str:
        return re.sub(r"\"|\'|\,|\.|\-", "", text)

    def get_unique_words(self) -> list[str]:
        counter = Counter(self.get_words())
        return [k for k, v in counter.items() if v == 1]

    def get_ngrams(self, n: int = 2) -> list[list[str]]:
        words = self.get_words()
        if n < 1 or n > len(words):
            return words

        ngrams = []
        for ngram_idx in range(0, len(words) - n + 1):
            ngrams.append(words[ngram_idx : ngram_idx + n])
        return ngrams
