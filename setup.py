
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## variables as per the requirements -
REPO_NAME = "ML Based Books Recommender System"
AUTHOR_USER_NAME = "Kgomotso Mongale"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Kgomotso Mongale",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eaze-dev/End-to-End-Book-Recommender-System",
    author_email="kgsotso16@gmail@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
