from setuptools import setup, find_packages

with open("README.md", "r") as f:  # lê o arquivo README.md
    page_description = f.read()  # lê o conteúdo do arquivo README.md

with open("requerimentos.txt") as f:
    requerimentos = (
        f.read().splitlines()
    )  # lê o arquivo requerimentos.txt e armazena em uma lista

setup(
    name="processamento_de_imagens",  # nome do pacote
    version="0.0.1",  # versão do pacote
    author="Junior de Freitas",  # autor do pacote
    description="Pacote para processamento de imagens",  # descrição do pacote
    long_description=page_description,  # descrição longa do pacote
    long_description_content_type="text/markdown",  # tipo de conteúdo da descrição longa
    url="https://github.com/juniordefreitas74/processamento_imagens.git",  # url do repositório do pacote
    packages=find_packages(),  # encontra todos os pacotes do projeto
    install_requires=requerimentos,  # requerimentos do pacote
    python_requires=">=3.8",  # versão mínima do Python
)
