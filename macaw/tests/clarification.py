import unittest
from macaw.core import clarifying_questions
from macaw.util.logging import Logger


class MyTestCase(unittest.TestCase):

    clarification_params = {'query_generation': 'simple',
                            'clarification_type': 'clariq',
                            'clariq_index': '/home/patrick-easton/Documents/CSA_Project_Patrick_Easton_Macaw/clarifying_questions/clariq',
                            'logger': Logger({})}

    clarification = clarifying_questions.get_clarifying_questions(params=clarification_params)

    def test_clarification_ralph_owen_brester(self):
        question = self.clarification.get_question("Tell me about of Ralph Owen Brester.")[0]
        self.assertEqual(question.clarification_needed, '1')
        self.assertIsNotNone(question.question_text)

    def test_clarification_uss_yorktown(self):
        question = self.clarification.get_question("tell me about uss yorktown charleston SC")[0]
        self.assertEqual(question.clarification_needed, '1')
        self.assertIsNotNone(question.question_text)

    def test_clarification_income_tax_return(self):
        question = self.clarification.get_question("I need information on income tax return online")[0]
        self.assertEqual(question.clarification_needed, '1')
        self.assertIsNotNone(question.question_text)

    def test_clarification_USDA_food_pyramid(self):
        question = self.clarification.get_question("What is USDA food pyramid")[0]
        self.assertEqual(question.clarification_needed, '1')
        self.assertIsNotNone(question.question_text)

    def test_clarification_obama_family_tree(self):
        question = self.clarification.get_question("Tell me about Obama family tree.")[0]
        self.assertEqual(question.clarification_needed, '2')
        self.assertIsNotNone(question.question_text)

    def test_clarification_fickle_creek_farm(self):
        question = self.clarification.get_question("What is Fickle Creek Farm.")[0]
        self.assertEqual(question.clarification_needed, '2')
        self.assertIsNotNone(question.question_text)

    def test_clarification_sonoma_medical_service(self):
        question = self.clarification.get_question("Tell me about sonoma county medical services.")[0]
        self.assertEqual(question.clarification_needed, '2')
        self.assertIsNotNone(question.question_text)

    def test_clarification_mayo_clinic_jacksonville(self):
        question = self.clarification.get_question("I'm looking for information about mayo clinic Jacksonville FL")[0]
        self.assertEqual(question.clarification_needed, '2')
        self.assertIsNotNone(question.question_text)

    def test_clarification_tv_on_computer(self):
        question = self.clarification.get_question("Tv on computer")[0]
        self.assertEqual(question.clarification_needed, '3')
        self.assertIsNotNone(question.question_text)

    def test_clarification_culpeper_cemetery(self):
        question = self.clarification.get_question("Tell me more about Culpeper National Cemetry")[0]
        self.assertEqual(question.clarification_needed, '3')
        self.assertIsNotNone(question.question_text)

    def test_clarification_butter_margarine(self):
        question = self.clarification.get_question("butter and margarine")[0]
        self.assertEqual(question.clarification_needed, '3')
        self.assertIsNotNone(question.question_text)

    def test_clarification_duchess_county_tourism(self):
        question = self.clarification.get_question("I'm looking for information on duchess county tourism")[0]
        self.assertEqual(question.clarification_needed, '3')
        self.assertIsNotNone(question.question_text)

    def test_clarification_source_of_the_nile(self):
        question = self.clarification.get_question("Tell me about source of the nile")[0]
        self.assertEqual(question.clarification_needed, '4')
        self.assertIsNotNone(question.question_text)

    def test_clarification_dinosaurs(self):
        question = self.clarification.get_question("I'm interested in dinosaurs")[0]
        self.assertEqual(question.clarification_needed, '4')
        self.assertIsNotNone(question.question_text)

    def test_clarification_iron(self):
        question = self.clarification.get_question("tell me about iron")[0]
        self.assertEqual(question.clarification_needed, '4')
        self.assertIsNotNone(question.question_text)

    def test_clarification_bellevue(self):
        question = self.clarification.get_question("Tell me about Bellevue.")[0]
        self.assertEqual(question.clarification_needed, '4')
        self.assertIsNotNone(question.clarification_needed)


if __name__ == '__main__':
    unittest.main()
