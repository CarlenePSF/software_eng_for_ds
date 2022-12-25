from .document import Document
from collections import Counter
import re


class SocialMedia(Document):
    """Analyze text data from social media

    :param text: social media text to analyze
    :ivar hashtag_counts: Counter object containing counts of hashtags used in text
    :ivar mention_counts: Counter object containing counts of @mentions used in text
    """
    def __init__(self, text):
        # call parent's __init__ method
        Document.__init__(self, text)
        # add attribute unique to SocialMedia class
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return Counter(re.findall(r'^#', self.text)).most_common(10)

    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return Counter(re.findall(r'^@', self.text)).most_common(10)



