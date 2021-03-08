from macaw.core.summariser.summariser import Summariser
from gensim.summarization.summarizer import summarize
from macaw.core.retrieval.doc import Document


class Gensim(Summariser):
    def __init__(self, params):
        super().__init__(params)

    def summarise(self, doc):
        if self.number_of_sentences(doc) > 5:
            summary = summarize(doc, ratio=0.2)
            return [Document(None, None, summary, 0)]
        return [Document(None, None, doc, 0)]

    def number_of_sentences(self, paragraph):
        return len(paragraph.split('.'))
