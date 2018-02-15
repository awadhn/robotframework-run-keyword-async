from setuptools import setup

setup(
    name = "robotframework-run-keyword-async",
    version = "1.0.8",
    description = "Generic Robot Framework library for asynchronous keyword or method execution",
    author = "Awadh Shukla",
    author_email = "shukla.awadh@gmail.com",
    license = "MIT",
    url = "https://github.com/awadhn/robotframework-run-keyword-async",
    download_url = "https://github.com/awadhn/robotframework-run-keyword-async",
    keywords = ["run-keyword-async", "async", "robotframework"],
    install_requires = ["robotframework >= 2.8.6"],
    packages = ["runKeywordAsync"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ]
)
