import sys
import os
import time
from robot.libraries.BuiltIn import BuiltIn
from robot.output.logger import LOGGER

class runKeywordAsync:
    def __init__(self):
        self._thread_pool = {}
        self._last_thread_handle = 1
        #self._robot_log_level = BuiltIn().get_variable_value("${LOG_LEVEL}")

    def run_method_async(self, keyword, *args, **kwargs):
        #BuiltIn().set_log_level("NONE")
        handle = self._last_thread_handle
        thread = self._threaded_method(keyword, *args, **kwargs)
        thread.start()
        self._thread_pool[handle] = thread
        self._last_thread_handle += 1
        return handle

    def run_keyword_async(self, keyword, *args):
        #BuiltIn().set_log_level("NONE")
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
              #BuiltIn().set_log_level(self._robot_log_level)
              for thread in self._thread_pool:
                  self._thread_pool[thread].terminate()
              raise Exception("Process " + str(thread) + " Failed")
        #BuiltIn().set_log_level(self._robot_log_level)
        self._thread_pool = {}
        self._last_thread_handle = 1
        return results

    def get_async_return(self, handle, timeout=60):
        timeout = int(timeout)
        if handle in self._thread_pool:
            try:
              result = self._thread_pool[handle].result_queue.get(True, timeout)
              del self._thread_pool[handle]
              BuiltIn().set_log_level(self._robot_log_level)
              return result
            except:
              raise Exception("Process " + str(handle) + " Failed")
        else:
            raise Exception("Passed Process id " + str(handle) + " is not a valid id")

    def _threaded_method(self, keyword, *args, **kwargs):
        from multiprocessing import Queue
        from multiprocessing import Process

        def wrapped_f(q, *args, **kwargs):
            ''' Calls the decorated function and puts the result in a queue '''
            ret = BuiltIn().call_method(keyword, *args, **kwargs)
            q.put(ret)

        q  = Queue()
        th = Process(target=wrapped_f, args=(q,)+args, kwargs=kwargs)
        th.result_queue = q
        return th

    def _threaded(self, keyword, *args):
        from multiprocessing import Queue
        from multiprocessing import Process

        def wrapped_f(q, *args):
            ''' Calls the decorated function and puts the result in a queue '''
            LOGGER.unregister_xml_logger()
            ret = BuiltIn().run_keyword(keyword, *args)
            q.put(ret)

        q  = Queue()
        th = Process(target=wrapped_f, args=(q,)+args)
        th.result_queue = q
        return th
