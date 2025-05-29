import time
import tracemalloc


def measure_performance(func, data):
    """
    Measures the execution time and peak memory usage of a function.

    Returns:
        (time_taken in ms, memory_used in KB)
    """
    tracemalloc.start()
    start_time = time.perf_counter()
    func(data.copy())
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    time_taken = (end_time - start_time) * 1000
    memory_used = peak / 1024

    return time_taken, memory_used
