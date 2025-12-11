import threading
import time

def worker(num):
    print(f"Thread {num} starting")
    time.sleep(1)
    print(f"Thread {num} finishing")

threads = []

for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
