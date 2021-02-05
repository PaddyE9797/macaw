from macaw.core.clarifying_questions.clariq import Clariq


def get_clarifying_questions(params):
    params['logger'].info('Clarifying Questions used for retrieval: ' + params['clarifying_questions'])
    if params['clarifying_questions'] == 'clariq':
        return Clariq(params)
    else:
        raise Exception('The requested clarifying questions do not exist')
