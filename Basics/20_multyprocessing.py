from multiprocessing import Process
import time

def worker(name):
    print(f"starting {name}")
    time.sleep(2)
    print(f"finished {name}")

if __name__ == "__main__":
    p1 = Process(target=worker, args=("Process-1",))
    p2 = Process(target=worker, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("all processes completed")