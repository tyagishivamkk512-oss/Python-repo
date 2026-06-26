# in threads

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for i in range(10):
        with lock:
            counter += 1
        
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)

# without lock both threas read counter at same time and increment at same so 
# the output maybe less than 20
# now only one thread can work at a time
# we can also use lock.acqire()
#           and lock.release() insted of with
#           we can also use lock.acquire(timeout = 5) it will keep acqiring lock for 5 sec