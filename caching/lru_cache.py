import time
from functools import lru_cache


@lru_cache(maxsize=128)  # maxsize 128 unique calls (based on arguments) to be cached
def slow_function(n):
    print(f"Computing slow_function({n})...")
    time.sleep(2)  # Simulates a slow operation
    return n * n


def timed_call(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    duration = end - start
    print(f"Result: {result} (executed in {duration:.4f} seconds)")
    return result


# Call with timing
timed_call(slow_function, 10)  # First call: ~2 seconds
timed_call(slow_function, 10)  # Cached: ~0 seconds
timed_call(slow_function, 5)   # First call: ~2 seconds
timed_call(slow_function, 5)   # Cached: ~0 seconds
