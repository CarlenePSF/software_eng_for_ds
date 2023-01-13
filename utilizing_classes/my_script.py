import text_analyzer
from text_analyzer.document import Document
from text_analyzer.social_media import SocialMedia
from collections import Counter

datacamp_tweets = """
 #datacamp 
 #datacamp 
 #datascience
 #datascience
 #datascience
 #datascience
 #code
 @elian
 @johnDoe
 @johnDoe
 @johnDoe
"""

# create a new document instance from data camp_tweets
# datacamp_doc = Document(datacamp_tweets)
#
# # print the first 5 tokens
# print(datacamp_doc.tokens)
# # print the top 5 most used words
# print(datacamp_doc.word_counts.most_common(5))
#
# social_media = SocialMedia(datacamp_tweets)
# print(social_media.hashtag_counts)
# print(social_media.mention_counts)


def sum_counters(counters):
    """Aggregate collections.Counter objects by summing counts

    :param counters: list/tuple of counters to sum
    :return: aggregated counters with counts summed

    #>>> d1 = text_analyzer.Document('1 2 fizz 4 buzz fizz 7 8')
    #>>> d2 = text_analyzer.Document('fizz buzz 11 fizz 13 14')
    #>>> sum_counters([d1.word_counts, d2.word_counts])
    Counter({'fizz': 4, 'buzz': 2, '1': 1, '2': 1, '4': 1, '7': 1, '8': 1, '11': 1, '13': 1, '14': 1})
    """
    return sum(counters, Counter())


d1 = text_analyzer.document.Document('1 2 fizz 4 buzz fizz 7 8')
d2 = text_analyzer.document.Document('fizz buzz 11 fizz 13 14')
print(sum_counters([d1.word_counts, d2.word_counts]))
