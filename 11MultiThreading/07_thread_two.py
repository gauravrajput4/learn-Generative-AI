import threading
import time

def prepare_chai(type_,wait_time):
    print(f"Preparing {type_}...")
    time.sleep(wait_time)
    print(f"Preparing {type_} done...")

t1=threading.Thread(target=prepare_chai,args=("Masala Chai",3))
t2=threading.Thread(target=prepare_chai,args=("Ginger Chai",4))
t3=threading.Thread(target=prepare_chai,args=("Elaichi Chai",5))
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
