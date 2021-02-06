from macaw.core.clarifying_questions.clariq import Clariq
from macaw.core.retrieval import query_generation


def get_clarifying_questions(params):
    params['logger'].info('Clarifying Questions used for retrieval: ' + params['clarification_type'])
    if params['query_generation'] == 'simple':
        q_generation = query_generation.SimpleQueryGeneration(params)
    else:
        raise Exception('The requested query generation model does not exist!')

    if params['clarification_type'] == 'clariq':
        return Clariq({'query_generation': q_generation,
                       'index': params['clariq_index'],
                       'logger': params['logger']})
    else:
        raise Exception('The requested clarifying questions do not exist')
