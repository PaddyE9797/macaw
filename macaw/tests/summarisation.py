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

    whoosh = retrieval.get_retrieval_model(params=retrieval_params)
    nltk = summariser.get_summariser(params=nltk_summariser_params)
    gensim = summariser.get_summariser(params=gensim_summariser_params)

    def test_summary_manhattan_project_1(self):
        doc = self.whoosh.retrieve("The Manhattan Project?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_manhattan_project_2(self):
        doc = self.whoosh.retrieve("Lets talk about the Manhattan Project?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_manhattan_project_3(self):
        doc = self.whoosh.retrieve("Tell me about the Manhattan Project?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_manhattan_project_4(self):
        doc = self.whoosh.retrieve("What is the Manhattan Project?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_manhattan_project_5(self):
        doc = self.whoosh.retrieve("What do you know about the Manhattan Project?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_retrieval_restorative_justice_1(self):
        doc = self.whoosh.retrieve("Restorative Justice?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_restorative_justice_2(self):
        doc = self.whoosh.retrieve("Lets talk about Restorative Justice?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_restorative_justice_3(self):
        doc = self.whoosh.retrieve("Tell me about Restorative Justice?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_restorative_justice_4(self):
        doc = self.whoosh.retrieve("What is Restorative Justice?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_restorative_justice_5(self):
        doc = self.whoosh.retrieve("What do you know about Restorative Justice?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_immigration_1(self):
        doc = self.whoosh.retrieve("Chinese Immigration?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_immigration_2(self):
        doc = self.whoosh.retrieve("Lets talk about Chinese Immigration?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_immigration_3(self):
        doc = self.whoosh.retrieve("Tell me about Chinese Immigration?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_retrieval_immigration_4(self):
        doc = self.whoosh.retrieve("How big is Chinese Immigration to America?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_retrieval_immigration_5(self):
        doc = self.whoosh.retrieve("What do you know about Chinese Immigration?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_medical_tourism_1(self):
        doc = self.whoosh.retrieve("Medical Tourism in Costa Rica?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_medical_tourism_2(self):
        doc = self.whoosh.retrieve("Lets talk about Medical Tourism in Costa Rica?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_medical_tourism_3(self):
        doc = self.whoosh.retrieve("Tell me about Medical Tourism in Costa Rica?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_summary_medical_tourism_4(self):
        doc = self.whoosh.retrieve("How prevalent is medical tourism in Costa Rica?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))

    def test_retrieval_medical_tourism_5(self):
        doc = self.whoosh.retrieve("What do you know about Medical Tourism in Costa Rica?")[0].text
        nltk_summary = self.nltk.summarise(doc)[0].text
        gensim_summary = self.gensim.summarise(doc)[0].text

        self.assertLessEqual(len(nltk_summary), 1000)
        self.assertLessEqual(len(nltk_summary), len(gensim_summary))


if __name__ == '__main__':
    unittest.main()
