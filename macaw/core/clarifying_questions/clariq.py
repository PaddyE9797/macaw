from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from macaw.core.clarifying_questions.question import Question


class Clariq:
    def __init__(self, params):
        self.params = params
        self.index = open_dir(self.params['index'])
        self.query_generation = params['query_generation']

    def get_results(self, conv_list):
        query = self.query_generation.get_query(conv_list)
        self.params['logger'].info('New query: ' + query)
        result_list = self.get_question(query)
        return result_list

    def get_question(self, query):
        questions = []
        with self.index.searcher() as s:
            q = QueryParser("initial_request", schema=self.index.schema).parse(query)
            results = s.search(q, limit=1)
            if len(results) > 0:
                for r in results:
                    questions.append(Question(r["question_id"], r["question"], r["clarification_need"]))
        return questions
