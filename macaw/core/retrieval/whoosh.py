"""
The Whoosh search engine.

Authors: Patrick Easton
"""

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh.qparser import OrGroup

from macaw.core.retrieval.doc import Document
from macaw.core.retrieval.search_engine import Retrieval
from gensim.summarization.summarizer import summarize

import re
import heapq
import nltk
nltk.download('punkt')
nltk.download('stopwords')


class Whoosh(Retrieval):
    def __init__(self, params):
        super().__init__(params)
        self.results_requested = self.params['results_requested'] if 'results_requested' in self.params else 1
        self.index = open_dir(self.params['index'])

    def retrieve(self, query):
        docs = []
        with self.index.searcher() as s:
            q = QueryParser("content", schema=self.index.schema, group=OrGroup).parse(query)
            results = s.search(q, limit=self.results_requested)
            for r in results:
                summary = self.summarise(r["content"])
                docs.append(Document(r["title"], r["url"], summary, r.score))
        return docs

    def retrieve_gensim(self, query):
        docs = []
        with self.index.searcher() as s:
            q = QueryParser("content", schema=self.index.schema, group=OrGroup).parse(query)
            results = s.search(q, limit=self.results_requested)
            for r in results:
                summary = self.summarise_gensim(r["content"])
                docs.append(Document(r["title"], r["url"], summary, r.score))
        return docs

    def summarise(self, doc_text):
        doc_text = re.sub(r'\[[0-9]*\]', ' ', doc_text)
        doc_text = re.sub(r'\s+', ' ', doc_text)

        formatted_doc_text = re.sub('[^a-zA-Z]', ' ', doc_text)
        formatted_doc_text = re.sub(r'\s+', ' ', formatted_doc_text)

        sentence_list = nltk.sent_tokenize(doc_text)
        stopwords = nltk.corpus.stopwords.words('english')

        word_frequencies = {}
        for word in nltk.word_tokenize(formatted_doc_text):
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1

        maximum_frequency = max(word_frequencies.values())

        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word] / maximum_frequency)

        sentence_scores = {}
        for sent in sentence_list:
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]

        summary_sentences = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary

    def summarise_gensim(self, doc_text):
        return summarize(doc_text)

    def get_doc_from_index(self, doc_id):
        doc = []
        with self.index.searcher() as s:
            q = QueryParser("title", schema=self.index.schema).parse(doc_id)
            r = s.search(q, limit=1)
            doc.append(Document(r["title"], r["url"], r["content"], r.score))
        return doc
