import os
import socket

#Checking the Ip adresses of incoming traffic
def check_ip():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind (("", 0))
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  s.settimeout(0.2)
  try:
    message, address = s.recvfrom(1024)
    return address[0]
  except socket.timeout:
    return None
    
#creating a dictionary to store the IP addresses that I want to block
blocked_ips = {}

#block traffic from specific addresses
def block_ip(ip_address):
  os.system("iptables -A INPUT -s " + ip_address + " -j DROP")
  blocked_ips[ip_address] = True
  
# check for incoming traffic from specific IP addreses
while True:
  ip_address = check_ip()
  if ip_address is not None and ip_address not in blocked_ips:
    block_ip(ip_address)
    

    print("Blocked IP address: " + ip_address)
