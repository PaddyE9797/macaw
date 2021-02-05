"""
The Whoosh search engine.

Authors: Patrick Easton
"""

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh.qparser import OrGroup

from macaw.core.retrieval.doc import Document
from macaw.core.retrieval.search_engine import Retrieval


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
                docs.append(Document(r["title"], r["url"], r["content"], r.score))
        return docs

    def get_doc_from_index(self, doc_id):
        doc = []
        with self.index.searcher() as s:
            q = QueryParser("title", schema=self.index.schema).parse(doc_id)
            r = s.search(q, limit=1)
            doc.append(Document(r["title"], r["url"], r["content"], r.score))
        return doc
