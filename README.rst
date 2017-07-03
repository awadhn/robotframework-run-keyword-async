Generic Robot Framework library for asynchronous keyword or method execution

Installation

If you have pip installed: pip3 install robotframework-run-keyword-async

Alternatively download directly from the Python Package Index: https://pypi.python.org/pypi/robotframework-run-keyword-async

Usage

Import into a test suite with:
Library runKeywordAsync
To run a keyword asynchronously:
${handle} Run Keyword Async <keyword name> <first argument> <second argument>
To wait for all keywords and retrieve the return value:
${return_value}=   Wait Async All   timeout=3
