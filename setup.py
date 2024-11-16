from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

REPO_NAME = "Twitter-Sentiment-Analysis"
AUTHOR_USER_NAME = "Yoyobun1"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["matplotlib","scikit-learn","numpy","pandas","nltk",""]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author = "Yoyobun1",
    descritpion = "A simple Twitter Sentiment analysis project",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/Yoyobun1/Twitter-Sentiment-Analysis",
    author_email = "marcgeorgenow@gmail.com",
    packages = [SRC_REPO],
    python_requires = ">=3.6",
    install_requires = LIST_OF_REQUIREMENTS,
)