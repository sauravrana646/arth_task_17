import socket
import threading


def rcv():
    r = socket.socket(family=socket.AF_INET , type=socket.SOCK_DGRAM)
    r.bind(("__your_ip_here__" , __your_port_here___))
    while True : 
        rd = r.recvfrom(4096)
        print(f"\n{rd[1][0]:>{90}s} : {rd[0].decode()}")      # f"{py:>{width}s} : {vg:>{width}s}"

def snd():
    s = socket.socket(family=socket.AF_INET , type=socket.SOCK_DGRAM)
    while True:
        data = input()
        s.sendto(data.encode(), ("__target_ip_here__" , __target_port_here___))
        input()
       
x = threading.Thread(target=snd)
y = threading.Thread(target=rcv)

x.start()
y.start()
