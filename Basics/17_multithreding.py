import threading
import time

def sleeping():
    time.sleep(8)
    print("now you're going to sleep")

def walking():
    time.sleep(4)
    print("you're walking")

def running():
    time.sleep(6)
    print("now you're running")

work1 = threading.Thread(target=sleeping)
work1.start()

work2 = threading.Thread(target=walking)
work2.start()

work3 = threading.Thread(target=running)
work3.start()

work1.join()
work2.join() # now it will join all 3 work 
work3.join()

time.sleep(1)
print("you've completed your routine")
# threding is to start multiple functions/tasks at once