from macaw.core.summariser.summariser import Summariser
from macaw.core.retrieval.doc import Document

import re
import heapq
import nltk
nltk.download('punkt')
nltk.download('stopwords')


class NLTK(Summariser):
    def __init__(self, params):
        super().__init__(params)

    def summarise(self, doc):
        doc_text = re.sub(r'\[[0-9]*\]', ' ', doc)
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
        return [Document(None, None, summary, 0)]
