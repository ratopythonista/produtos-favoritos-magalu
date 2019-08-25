from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='produtosfavoritos',
    version='0.1.0',
    description='Desafio Técnico - LuizaLabs/Magalu',
    long_description=long_description, 
    long_description_content_type='text/markdown',
    url='https://github.com/ratopythonista/produtos-favoritos-magalu',
    author='Rodrigo Guimarães Araújo',
    author_email='ratopythonista@gmail.com',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.6.*',
    install_requires=[
            'flask==1.1.1',
            'flask_restful==0.3.7',
            'requests==2.22.0',
            'pymongo==3.9.0',
            'loguru==0.3.2',
            'flask_cors==3.0.8',
            'flasgger==0.9.3',
            'gunicorn==19.9.0'
        ],
)
