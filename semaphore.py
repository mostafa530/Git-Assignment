import threading
import time

sem = threading.Semaphore(2)

def worker(num):
    print(f"Worker {num} waiting")
    with sem:
        print(f"Worker {num} entered critical section")
        time.sleep(1)
        print(f"Worker {num} leaving")

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
