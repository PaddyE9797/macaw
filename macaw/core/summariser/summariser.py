from abc import ABC, abstractmethod


class Summariser(ABC):
    @abstractmethod
    def __init__(self, params):
        self.params = params

    @abstractmethod
    def summarise(self, doc):
        pass

    @abstractmethod
    def number_of_sentences(self, paragraph):
        pass
