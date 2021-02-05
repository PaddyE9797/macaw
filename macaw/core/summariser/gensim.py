from macaw.core.summariser.summariser import Summariser
from gensim.summarization.summarizer import summarize
from macaw.core.retrieval.doc import Document


class Gensim(Summariser):
    def __init__(self, params):
        super().__init__(params)

    def summarise(self, doc):
        summary = summarize(doc, ratio=0.2)
        return [Document(None, None, summary, 0)]
