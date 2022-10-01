from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Processador_de_imagem",
    version="0.0.1",
    author="Paulo Silva",
    author_email="paulo_rikrdo@hotmail.com",
    description="Pacote de processamento de imagem usando Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prikrdo/processador_de_imagem",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)