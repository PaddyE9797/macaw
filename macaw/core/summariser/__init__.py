from macaw.core.summariser.gensim import Gensim
from macaw.core.summariser.nltk import NLTK


def get_summariser(params):
    params['logger'].info('The summariser used for summarisation is: ' + params['summariser'])
    if params['summariser'] == 'gensim':
        return Gensim(params)
    elif params['summariser'] == 'nltk':
        return NLTK(params)
    else:
        raise Exception("Summariser type is not supported")
