import nltk
import newspaper
import random


def main():
    nltk.download("punkt", quiet=True)

    bbc_news = newspaper.build(
        "https://www.bbc.co.uk",
        MAX_SUMMARY_SENT=2,
        memoize_articles=False,
    )

    article = bbc_news.articles[random.randrange(0, bbc_news.size())]

    article.download()
    article.parse()
    article.nlp()

    print(f"Title:{article.title}")
    print(f"Summary:{article.summary}")
