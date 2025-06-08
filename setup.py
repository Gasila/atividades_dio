from setuptools import setup, find_packages

# Ler o README.md para usar como descrição longa
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Ler as dependências do arquivo requirements.txt (opcional)
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="nome_do_pacote",               # Nome do seu pacote
    version="0.1.0",                     # Versão inicial do pacote
    author="Seu Nome",                   # Autor do pacote
    author_email="seu_email@example.com",  # Email do autor
    description="Descrição curta do pacote",
    long_description=long_description,  # Descrição longa do README
    long_description_content_type="text/markdown",  # Tipo do README (Markdown)
    url="https://github.com/seu_usuario/seu_projeto",  # Link do repositório
    packages=find_packages(),            # Descobre todos os pacotes automaticamente
    install_requires=requirements,       # Lista de dependências
    python_requires='>=3.8',             # Versão mínima do Python suportada
    classifiers=[                       # Metadados opcionais para o PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
