import sys
import os
import time
from robot.libraries.BuiltIn import BuiltIn

class runKeywordAsync:
    def __init__(self):
        self._thread_pool = {}
        self._last_thread_handle = 1

    def run_method_async(self, keyword, *args, **kwargs):
        handle = self._last_thread_handle
        thread = self._threaded_method(keyword, *args, **kwargs)
        thread.start()
        self._thread_pool[handle] = thread
        self._last_thread_handle += 1
        return handle

    def run_keyword_async(self, keyword, *args):
        handle = self._last_thread_handle
        thread = self._threaded(keyword, *args)
        thread.start()
        self._thread_pool[handle] = thread
        self._last_thread_handle += 1
        return handle

    def wait_async_all(self, timeout=60):
        timeout = int(timeout)
        results = []
        for thread in self._thread_pool:
            try:
              result = self._thread_pool[thread].result_queue.get(True, timeout)
              results.append(result)
            except:
              raise Exception("Thread " + str(thread) + " Failed")
        return results

    def get_async_return(self, handle, timeout=60):
        timeout = int(timeout)
        if handle in self._thread_pool:
            try:
              result = self._thread_pool[handle].result_queue.get(True, timeout)
              del self._thread_pool[handle]
              return result
            except:
              raise Exception("Thread " + str(handle) + " Failed")
        else:
            raise Exception("Passed Thread id " + str(handle) + " is not a valid id")

    def _threaded_method(self, keyword, *args, **kwargs):
        from multiprocessing import Queue
        from threading import Thread

        def wrapped_f(q, *args, **kwargs):
            ''' Calls the decorated function and puts the result in a queue '''
            ret = BuiltIn().call_method(keyword, *args, **kwargs)
            q.put(ret)

        q = Queue()
        th = Thread(target=wrapped_f, args=(q,)+args, kwargs=kwargs)
        th.result_queue = q
        return th

    def _threaded(self, keyword, *args):
        from multiprocessing import Queue
        from threading import Thread
    
        def wrapped_f(q, *args):
            ''' Calls the decorated function and puts the result in a queue '''
            ret = BuiltIn().run_keyword(keyword, *args)
            q.put(ret)

        q = Queue()
        th = Thread(target=wrapped_f, args=(q,)+args)
        th.result_queue = q
        return th
