import re
from collections import Counter


class Document:
    """Analyze text data

    :param text: text to analyze
    :ivar text: text originally passed to the instance on creation
    :ivar tokens: Parsed list of words from text
    :ivar word_counts: Counter containing counts of hashtags used in text
    """

    def __init__(self, text):
        self.text = text
        # Tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # Perform word count with non-public count_words method
        self.word_counts = self._count_words()

    def _tokenize(self):
        return self.text.split()

    # non-public method to tally document's word counts with Counter
    def _count_words(self):
        return Counter(self.tokens)

    def filter_word_counts(self, first_char=None):
        return self.word_counts.most_common(first_char)



