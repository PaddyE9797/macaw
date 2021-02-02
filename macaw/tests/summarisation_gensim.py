import unittest
from macaw.core import retrieval
from macaw.util.logging import Logger


class SummarisationGensimTestCases(unittest.TestCase):
    retrieval_params = {'search_engine': 'whoosh',
                        'query_generation': 'simple',
                        'col_index': '/home/patrick-easton/Documents/CSA_Project_Patrick_Easton_Macaw/whoosh/indexdir',
                        'results_requested': 3,
                        'logger': Logger({})}

    retrieval_params['logger'].info(retrieval_params)

    def test_summary_manhattan_project_1(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("The Manhattan Project?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_manhattan_project_2(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("Lets talk about the Manhattan Project?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_manhattan_project_3(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("Tell me about the Manhattan Project?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_manhattan_project_4(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("What is the Manhattan Project?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_manhattan_project_5(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("What do you know about the Manhattan Project?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_restorative_justice_1(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("Restorative Justice?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_restorative_justice_2(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("Lets talk about Restorative Justice?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_restorative_justice_3(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("Tell me about Restorative Justice?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_restorative_justice_4(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("What is Restorative Justice?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_restorative_justice_5(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("What do you know about Restorative Justice?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_immigration_1(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("Chinese Immigration?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_immigration_2(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("Lets talk about Chinese Immigration?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_immigration_3(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("Tell me about Chinese Immigration?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_immigration_4(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("How big is Chinese Immigration to America?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_immigration_5(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("What do you know about Chinese Immigration?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_medical_tourism_1(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("Medical Tourism in Costa Rica?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_medical_tourism_2(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("Lets talk about Medical Tourism in Costa Rica?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_medical_tourism_3(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("Tell me about Medical Tourism in Costa Rica?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_medical_tourism_4(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("How prevalent is medical tourism in Costa Rica?")
        self.assertLessEqual(len(doc[0].text), 1000)

    def test_retrieval_medical_tourism_5(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        doc = whoosh.retrieve_gensim("What do you know about Medical Tourism in Costa Rica?")
        self.assertLessEqual(len(doc[0].text), 1000)


if __name__ == '__main__':
    unittest.main()
