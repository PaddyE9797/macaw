from setuptools import setup

setup(
    name='macaw',
    version='0.1',
    packages=['macaw', 'macaw.core', 'macaw.core.mrc', 'macaw.core.retrieval', 'macaw.core.input_handler',
              'macaw.core.output_handler', 'macaw.core.interaction_handler', 'macaw.util', 'macaw.interface',
              'macaw.core.summariser', 'macaw.core.clarifying_questions'],
    url='https://github.com/microsoft/macaw/',
    license='MIT',
    author='Hamed Zamani',
    author_email='hazamani@microsoft.com',
    description='An extensible framework for conversational information seeking research'
)
