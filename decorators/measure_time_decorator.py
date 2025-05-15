import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper


@measure_time
def compute():
    total = 0
    for i in range(1000000):
        total += i
    return total


print(compute())
