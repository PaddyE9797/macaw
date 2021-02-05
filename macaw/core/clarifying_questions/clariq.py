from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from macaw.core.clarifying_questions.question import Question


class Clariq:
    def __init__(self, params):
        self.params = params
        self.index = open_dir(self.params['clariq_index'])

    def get_question(self, query):
        questions = []
        with self.index.searcher() as s:
            q = QueryParser("initial_request", schema=self.index.schema).parse(query)
            results = s.search(q, limit=1)
            if len(results) > 0:
                for r in results:
                    questions.append(Question(r["question_id"], r["question"], r["clarification_needed"]))
        return questions
