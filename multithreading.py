import threading

def task():
    for i in range(3):
        print("Task running")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
