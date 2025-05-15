from concurrent.futures.thread import ThreadPoolExecutor
import time


def task(n):
    print(f"Working on task {n}")
    time.sleep(2)
    print(f"Finished task {n}")


with ThreadPoolExecutor(max_workers=2) as executor:
    for i in range(6):
        executor.submit(task, i)
