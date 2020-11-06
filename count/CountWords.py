from textlib.Text import PageText
from rank_bm25 import BM25Okapi, BM25L, BM25
from textlib.Clear import ClearText


class CountModel:
    def __init__(self, url):
        self.url = url

    def get_the_corpus(self, model, query=0):
        # Получаем корпус всех слов
        corpus = PageText(model)
        good_corpus = corpus.writeFile(self.url)
        corpus_clear = ClearText(good_corpus)
        future_corpus = corpus_clear.corpus_text()

        # Делим на предложения на списки
        tokenized_corpus = [doc.split(" ") for doc in future_corpus]
        bm25 = BM25Okapi(tokenized_corpus)

        # Даем оценку по NumPy
        tokenized_query = query.split(" ")
        #doc_scores = bm25.get_scores(tokenized_query)

        # Узнаем по ключу релевантное предложение NumPy
        result = bm25.get_top_n(tokenized_query, future_corpus, n=1)

        print(result, self.url)
