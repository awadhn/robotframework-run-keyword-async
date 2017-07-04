**Description**
 Generic Robot Framework library for asynchronous keyword or method execution
 This module takes keyword as input and runs it as an independent thread. This module also provide a mechanism to wait for all the spawned thread with a timeout and returns a list containing result.

**Installation**

If you have pip installed:
 pip3 install robotframework-run-keyword-async

Alternatively download directly from the Python Package Index:  
 https://pypi.python.org/pypi/robotframework-run-keyword-async

**Usage**

**1. Import into a test suite with:**
     Library runKeywordAsync 

**2. To run a keyword asynchronously:**                
     ${handle}=   Run Keyword Async   <keyword name>   <first argument>   <second argument>
       (Note: It takes only args as arguments, kwargs is not supported) 

**3. To wait for all keywords and retrieve the return value:** 
     ${return_value}=   Wait Async All   timeout=3
       (Note: timeout is an optional parameter, default timeout is 60 seconds)
