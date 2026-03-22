import threading

counter=0

lock=threading.Lock()

def increament():
    global counter
    for _ in range(100000):
        with lock:
            counter+=1

threadsc=[threading.Thread(target=increament) for _ in range(10)]
[t.start() for t in  threadsc]
[t.join() for t in threadsc]

print(f"Final Counter: {counter} ")