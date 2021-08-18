import argparse
from socket import *
import time
import ipaddress

startTime = time.time()

parser = argparse.ArgumentParser()
parser.add_argument('target', help="add the IP of the target")
args = parser.parse_args()

def scan(target):
    t_IP = target
    print ('Starting scan on host: ', t_IP)
    for i in range(0, 50000):
        s = socket(AF_INET, SOCK_STREAM)
       
        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            print ('%d/tcp: OPEN' % (i,))
        s.close()

if "-" in args.target:
    IP_range = args.target.split('-') 
    start_ip = ipaddress.IPv4Address(IP_range[0])
    end_ip = ipaddress.IPv4Address(IP_range[1])
    for ip_int in range(int(start_ip), int(end_ip)):
        print(ipaddress.IPv4Address(ip_int))
        scan(ip_int)
else:
    scan(args.target)

print('Time taken:', time.time() - startTime)
