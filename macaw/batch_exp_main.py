"""
The main file for an experimental CIS with batch interaction support.
Authors: Hamed Zamani (hazamani@microsoft.com)
"""

from macaw.cis import CIS
from macaw.core import mrc, retrieval, summariser, clarifying_questions
from macaw.core.input_handler.action_detection import RequestDispatcher
from macaw.core.output_handler import naive_output_selection
from macaw.util.logging import Logger


class ConvSearch(CIS):
    def __init__(self, params):
        super().__init__(params)
        self.logger = params['logger']
        self.logger.info('Conversational QA Model... starting up...')
        self.retrieval = retrieval.get_retrieval_model(params=self.params)
        self.qa = mrc.get_mrc_model(params=self.params)
        self.summariser = summariser.get_summariser(params=self.params)
        self.clarification = clarifying_questions.get_clarifying_questions(params=self.params)
        self.params['actions'] = {'retrieval': self.retrieval, 'qa': self.qa, 'summary': self.summariser,
                                  'clarify': self.clarification}
        self.request_dispatcher = RequestDispatcher(self.params)
        self.output_selection = naive_output_selection.NaiveOutputProcessing({})

    def request_handler_func(self, conv_list):
        # identify action
        self.logger.info(conv_list)
        dispatcher_output = self.request_dispatcher.dispatch(conv_list)
        output_msg = self.output_selection.get_output(conv_list, dispatcher_output)
        return output_msg

    def run(self):
        self.interface.run()


if __name__ == '__main__':
    basic_params = {'timeout': 120,  # timeout is in terms of second.
                    'mode': 'exp',
                    'logger': Logger({})}  # mode can be either live or exp.

    interface_params = {'interface': 'fileio',
                        'input_file_path': '/home/patrick-easton/Documents/CSA_Project_Patrick_Easton_Macaw/macaw/data/example_retrieval_input.txt',
                        'output_file_path': '/home/patrick-easton/Documents/CSA_Project_Patrick_Easton_Macaw/macaw/data/example_retrieval_output.txt',
                        'output_format': 'trec'}

    retrieval_params = {'query_generation': 'simple',
                        'search_engine': 'whoosh',  # 'bing' or 'indri'
                        'use_coref': False,  # True, if query generator can use coreference resolution, otherwise False.
                        'bing_key': '40e200c689cf44e4a5e117f697b5934a',  # only for Bing Web Search
                        'search_engine_path': 'PATH_TO_INDRI',  # only for Indri
                        'col_index': '/home/patrick-easton/Documents/CSA_Project_Patrick_Easton_Macaw/whoosh/indexdir',   # only for Indri
                        'col_text_format': 'trectext',  # trectext or trecweb. Only for Indri.
                        'results_requested': 3}

    mrc_params = {'mrc': 'drqa',
                  'mrc_model_path': '/home/patrick-easton/Documents/CSA_Project_Patrick_Easton_Macaw/DrQA/data/reader/multitask.mdl',
                  'mrc_path': '/home/patrick-easton/Documents/CSA_Project_Patrick_Easton_Macaw/DrQA',
                  'corenlp_path': '/home/patrick-easton/Documents/CSA_Project_Patrick_Easton_Macaw/stanford-corenlp-full-2017-06-09',
                  'qa_results_requested': 3}

    summariser_params = {'summariser': 'gensim'}

    clarification_params = {'clarification_type': 'clariq',
                            'clariq_index': '/home/patrick-easton/Documents/CSA_Project_Patrick_Easton_Macaw/clarifying_questions/clariq'}

    params = {**basic_params, **interface_params, **retrieval_params, **mrc_params, **summariser_params,
              **clarification_params}
    basic_params['logger'].info(params)
    ConvSearch(params).run()
