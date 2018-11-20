
import socket
import threading

from queue import Queue

print_lock = threading.Lock()

target = '192.168.0.253'

def portscan(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('Port',port,'is open!!')

        con.close()

    except:
        pass

def threader():
    while True:
        worker=q.get()
        portscan(worker)
        q.task_done()

q = Queue()
for x in range(30):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

for worker in range(1,6000):
    q.put(worker)

q.join()
