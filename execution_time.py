import time

def execution_time(func):
    def wrapped(*args, **kwargs):
        time_start = time.time()
        res = func(*args, **kwargs)
        time_finish = time.time()
        execution_time = time_finish - time_start
        print("Script execution time: %s sec" % execution_time)
        return res
    return wrapped