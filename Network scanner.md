For this part of the project, we will be building a network scanner, I don't have the necessary permissions to scan the networks near me as it is illegal to do so. Since this is a research project, I've stated the ways in which a network scanner can help people mitigate security risks and now I am going to write code that would scan the a nearby IP and Mac address. For necessary permissions on scanning nearby networks, using sudo on a unix based system would do the trick. At the end, I'll attach a link to my code and the sudo command that would be used like this if we were to access the networks on a unix based system(sudo python main.py). I am still trying to build a Kali linux Virtual machine on my mac but it won't install so as I work on that in order to incoperate "sudo" to my code and get the necessary permissions to scan nearby networks, I am going to talk about the step by step process it takes to build a network scanner in python.

First we have to install the scapy library, I'll install it using the "pip install scapy" command to install the scapy library and then i'll write this command to import packets/essential methods into the system(from scapy.all import ARP, Ether, srp).
 Next, we'll make an ARP request. The network scanner will send the ARP request indicating who has some specific IP address, let's say "192.168.1.1", the owner of that IP address ( the target ) will automatically respond saying that he is "192.168.1.1", with that response, the MAC address will also be included in the packet, this allows us to successfully retrieve all network users' IP and MAC addresses simultaneously when we send a broadcast packet (sending a packet to all the devices in the network).

For the next part of my code, I'll craft the packets. Now that we have created these packets, we need to send them using srp() function which sends and receives packets at layer 2, we set the timeout to 3 so the script won't get stuck.

The result now is a list of pairs that is of the format (sent_packet, received_packet), let's iterate over them. Now all we need to do is to print this list we have just filled. and the code is complete.

For access to my code, here is the link(https://replit.com/@LarnelleAnkunda/SECURITY#main.py)

I will dig deeper into this part of the project by scanning into my own personal network when I'm done installing my virtual machine. That's how I'll be able to provide an output.




