from setuptools import setup, find_packages

setup(
    name="chroma_research",
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
    ],
    author="Brandon A. Smith",
    author_email="brandonsmithpmpuk@gmail.com",
    description="A package for text chunking and benchmarking.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/chroma_research",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data={
        'chroma_research': ['benchmarking/general_benchmark_data/corpora/*']
    },
    python_requires='>=3.6',
)
