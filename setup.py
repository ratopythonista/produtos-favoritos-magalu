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
    author_email='ratopythonista@gmail.com',  # Optional
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.6.*',
    install_requires=[
            'peppercorn'
        ],
)
