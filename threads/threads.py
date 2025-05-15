import threading
import time


def worker(name, seconds):
    print(f"Thread {name} starting")
    time.sleep(seconds)
    print(f"Thread {name} finished after {seconds} seconds")


start_time = time.perf_counter()

t1 = threading.Thread(target=worker, args=("First thread", 3))
t2 = threading.Thread(target=worker, args=("Second thread", 2))
t3 = threading.Thread(target=worker, args=("Third thread", 1))

t1.start()
t2.start()
t3.start()

# Wait until threads are finished
t1.join()
t2.join()
t3.join()

end_time = time.perf_counter()
elapsed = end_time - start_time

print(f"All threads completed in {elapsed:.2f} seconds.")
