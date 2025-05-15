import time
from concurrent.futures import ThreadPoolExecutor


def worker(name, seconds):
    print(f"{name} started")
    time.sleep(seconds)
    print(f"{name} finished")
    return f"{name} ran for {seconds} seconds"


# Create a thread pool with 3 workers (workers are threads)
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit multiple tasks to the pool
    futures = [
        executor.submit(worker, f"Task {i}", i)
        for i in range(1, 6)  # Tasks with durations 1 to 5 seconds
    ]

    # Wait for all tasks to complete and get their results
    for future in futures:
        result = future.result()  # Blocks until the result is available
        print("Result:", result)
