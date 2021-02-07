from abc import ABC, abstractmethod


class Clarification(ABC):
    @abstractmethod
    def __init__(self, params):
        self.params = params
        self.query_generation = self.params['query_generation']

    @abstractmethod
    def get_question(self, query):
        pass

    def get_results(self, conv_list):
        query = self.query_generation.get_query(conv_list)
        self.params['logger'].info('New query: ' + query)
        result_list = self.get_question(query)
        return result_list
