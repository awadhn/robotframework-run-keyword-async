from setuptools import setup

setup(
    name = "robotframework-run-keyword-async",
    version = "1.0.0",
    description = "Generic Robot Framework library for asynchronous keyword or method execution",
    author = "Awadh Shukla",
    author_email = "shukla.awadh@gmail.com",
    license = "MIT",
    url = "https://github.com/Awadh/robotframework-run-keyword-async",
    download_url = "https://github.com/Awadh/robotframework-run-keyword-async",
    keywords = ["async", "robotframework"],
    install_requires = ["robotframework >= 2.8.6"],
    packages = ["KeywordAsyncLibrary"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ]
)
