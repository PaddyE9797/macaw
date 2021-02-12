import unittest
from macaw.core import retrieval, summariser
from macaw.util.logging import Logger


class SummarisationTestCases(unittest.TestCase):
    retrieval_params = {'search_engine': 'whoosh',
                        'query_generation': 'simple',
                        'col_index': '/home/patrick-easton/Documents/CSA_Project_Patrick_Easton_Macaw/whoosh/indexdir',
                        'results_requested': 3,
                        'logger': Logger({})}

    nltk_summariser_params = {'summariser': 'nltk',
                              'logger': Logger({})}

    gensim_summariser_params = {'summariser': 'gensim',
                                'logger': Logger({})}

    def test_summary_manhattan_project_1(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        nltk = summariser.get_summariser(params=self.nltk_summariser_params)
        gensim = summariser.get_summariser(params=self.gensim_summariser_params)

        doc = whoosh.retrieve("The Manhattan Project?")[0].text
        nltk_summary = nltk.summarise(doc)[0].text
        gensim_summary = gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))


if __name__ == '__main__':
    unittest.main()
