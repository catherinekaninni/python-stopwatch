import time
from xml.dom.pulldom import END_ELEMENT
while True:
    try:
        input("Press Enter to continue,CTRL-c To exist")
        start_time=time.time()
        print("Timer has started")
        while True:
            print("time elapsed=:",round(time.time()-start_time,0),'secs',end='\n')
            time.sleep(1)
    except KeyboardInterrupt:
        print("Timer has stopped")
        end_time=time.time()
        print("The time elapsed is",round(end_time-start_time,2),'secs')
        break

    