import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    with lock1:
        print("Task1 got Lock1")
        time.sleep(1)
        with lock2:
            print("Task1 got Lock2")

def task2():
    with lock2:
        print("Task2 got Lock2")
        time.sleep(1)
        with lock1:
            print("Task2 got Lock1")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
