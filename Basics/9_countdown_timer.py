import time

# time.sleep(5) 
# print("hello ji") now it will get printed after 5 seconds of compilation 

times = int(input("Enter time in seconds: "))

for i in range(times,0,-1):
    second = i%60
    mins = int((i/60)%60)  #division in python always gives float
    hrs = int((i/3600)%60)

    print(f"{hrs:02}:{mins:02}:{second:02}")
    time.sleep(1)

print("Time's Up!")
    