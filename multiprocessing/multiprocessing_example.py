import multiprocessing
import time


def compute():
    print(f"Process {multiprocessing.current_process().name} starting")
    total = 0
    for _ in range(10**7):
        total += 1
    print(f"Process {multiprocessing.current_process().name} finished")


if __name__ == "__main__":
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=compute, name="Process 1")
    p2 = multiprocessing.Process(target=compute, name="Process 2")

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds")
