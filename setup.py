from setuptools import setup, find_packages

setup(
    name="chunking_evaluation",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tiktoken",
        "fuzzywuzzy",
        "pandas",
        "numpy",
        "tqdm",
        "chromadb",
        "python-Levenshtein",
        "openai",
        "anthropic",
        "attrs",
        "pytest"
    ],
    author="Brandon A. Smith",
    author_email="brandonsmithpmpuk@gmail.com",
    description="A package to evaluate multiple chunking methods. It also provides two new chunking methods.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/chunking_evaluation",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data={
        'chunking_evaluation': ['evaluation_framework/general_evaluation_data/**/*', 'evaluation_framework/prompts/**/*']
    },
    python_requires='>=3.6',
)
