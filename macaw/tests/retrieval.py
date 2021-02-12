import unittest
from macaw.core import retrieval
from macaw.util.logging import Logger


class RetrievalTestCases(unittest.TestCase):
    retrieval_params = {'search_engine': 'whoosh',
                        'query_generation': 'simple',
                        'col_index': '/home/patrick-easton/Documents/CSA_Project_Patrick_Easton_Macaw/whoosh/indexdir',
                        'results_requested': 3,
                        'logger': Logger({})}

    retrieval_params['logger'].info(retrieval_params)

    def test_retrieval_manhattan_project_1(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("The Manhattan Project?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_manhattan_project_2(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("Lets talk about the Manhattan Project?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_manhattan_project_3(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("Tell me about the Manhattan Project?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_manhattan_project_4(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("What is the Manhattan Project?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_manhattan_project_5(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("What do you know about the Manhattan Project?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_restorative_justice_1(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("Restorative Justice?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_restorative_justice_2(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("Lets talk about Restorative Justice?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_restorative_justice_3(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("Tell me about Restorative Justice?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_restorative_justice_4(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("What is Restorative Justice?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_restorative_justice_5(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("What do you know about Restorative Justice?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_immigration_1(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("Chinese Immigration?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_immigration_2(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("Lets talk about Chinese Immigration?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_immigration_3(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("Tell me about Chinese Immigration?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_immigration_4(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("How big is Chinese Immigration to America?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_immigration_5(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("What do you know about Chinese Immigration?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_medical_tourism_1(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("Medical Tourism in Costa Rica?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_medical_tourism_2(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("Lets talk about Medical Tourism in Costa Rica?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_medical_tourism_3(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("Tell me about Medical Tourism in Costa Rica?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_medical_tourism_4(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("How prevalent is medical tourism in Costa Rica?")
        self.assertEqual(len(docs), 3)

    def test_retrieval_medical_tourism_5(self):
        whoosh = retrieval.get_retrieval_model(params=self.retrieval_params)
        docs = whoosh.retrieve("What do you know about Medical Tourism in Costa Rica?")
        self.assertEqual(len(docs), 3)


if __name__ == '__main__':
    unittest.main()
