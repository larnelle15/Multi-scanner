from scapy.all import ARP, Ether, srp

target_ip = "192.168.1.1/24"
#Crafting ARP packets 
#IP address for the target machine
arp = ARP(pdst = target_ip)
#create the ethernet broadcast packet
#broadcasting to all the clients in the network
ether = Ether(dst = "ff:ff:ff:ff:ff:ff")
#stacking the arp and ether packets
packet = ether/arp
#sending the packet and setting the timeout so the script doesn't hang
result = srp(packet, timeout = 3, verbose=0)[0]
#iterating over a list of pairs
clients = []
for sent, received in result:
  clients.append({'ip': received.psrc, 'mac': received.hwsrc})
  pass
#printing the list of clients
print("Available clients in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))