"""
New requirements. You need to be able to check memory usage of any script. 
    To check memory usage of a script you can do something like this:

        > start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        > end_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) - start_mem

    And you can read about the resource module by starting your interpretor and write:

        > import resource 
        > help(resource)
"""
import resource


def memory_usage_profiler(func):
    def wrapper(num):
        start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss # ru.max_rss returns the maximum resident set size
        # A process's resident set size is the amount of memory that belongs to it,
        # and is currently present (resident) in RAM (real RAM, not swapped or otherwise not-resident).
        func(num)
        end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - start_mem
    
        return f'{end_mem} kb of memory allocated to this process'
    return wrapper

@memory_usage_profiler
def looping(num):

    text = ""

    # the higher the number, the longer more memory is allocated
    for i in range(100000):
        text += "HEY "

    for i in range(num):
        if i % (num/10) == 0:
            print(i)
    