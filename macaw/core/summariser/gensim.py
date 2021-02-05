from gensim.summarization import summarizer
from macaw.core.summariser import summariser
from macaw.core.retrieval.doc import Document


class Gensim(summariser):
    def __init__(self, params):
        super().__init__(params)

    def summarise(self, doc):
        summary = summarizer.summarize(doc, ratio=0.2)
        return [Document(None, None, summary, 0)]
