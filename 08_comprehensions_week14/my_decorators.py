import time
import resource

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Time spent:', end - start)
    return wrapper

def memory_profiler(func):
    def wrapper(*args, **kwargs):
        start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss # ru.max_rss returns the maximum resident set size
        # A process's resident set size is the amount of memory that belongs to it,
        # and is currently present (resident) in RAM (real RAM, not swapped or otherwise not-resident).
        func(*args, **kwargs)
        end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - start_mem
    
        return f'{end_mem} kb of memory allocated to this process'
    return wrapper