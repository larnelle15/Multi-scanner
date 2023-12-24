This is the most efficient scanner for ethical hacking and mitigating security risks through penetration testing. I don't have the necessary permissions to scan nearby networks but I can use "sudo" for elevated script privileges. It's easier to run sudo on a kali linux operating system for more efficient results. I'm still working on this part of the project in terms of building a virtual machine for Kali linux but I've written my code and commented my thought process so here is step one:

First, I'll install scapy library using the (pip install scapy) shell script. After that, I'm going to use pandas for printing in a more favourable and nice format. I'll use the (pip install pandas) shell script. Now the only way in which the code, I am going to write will work is if im using monitor mode on my network interface and I'd have to install aircrack-ng which usually comes pre-installed in Kali linux(another advantage of using Kali linux). Now i'd run the "airmon-ng start wlan0" shell script followed by the "iwconfig or ifconfig" shell script to check my interface. That's how you can tell that your interace is now in monitor mode. We can also use the "sudo iwconfig wlan0 mode monitor" shell script to change the network card to monitor code.

Now, we'll write the code. Let's get started by opening up a new Python file and importing the necessary modules, then, we need to initialize an empty data frame that stores our networks. So I've set the BSSID (MAC address of the access point) as the index of each row, as it is unique for every device.

In the Scapy library, we can use the sniff() function, which takes the callback function that is executed whenever a packet is sniffed, I'm now going to implement this function.

This callback makes sure that the sniffed packet has a beacon layer on it, if it is the case, then it will extract the BSSID, SSID (name of access point), signal, and some stats. Scapy's Dot11Beacon class has the awesome network_stats() function that extracts some useful information from the network, such as the channel, rates, and encryption type. Finally, we add these information to the dataframe with the BSSID as the index.

In encountering some networks that don't have the SSID (ssid equals to ""), this is an indicator that it's a hidden network. In hidden networks, the access point leaves the info field blank to hide the discovery of the network name.

Now we need a way to visualize this dataframe. Since we're going to use sniff() function (which blocks and start sniffing in the main thread), we need to use a separate thread to print the content of networks dataframe, the code I'm going to write now does that. and then I will write the main code with my thought process documented in comments. 

Now, after executing this, from what I learned in my cybersecurity class, I will notice not all nearby networks are available. That's because I'm listening on one WLAN channel only. We can use the iwconfig command to change the channel. I will now create a function for this.

For instance if I wanted to change to channel 2, this would be my shell script(iwconfig wlan0mon channel 2)

The function i will now write will change channels incrementally from 1 to 14 every 0.5 seconds, spawning the daemon thread that runs this function. Since, we set the daemon attribute of the thread to True, so this thread will end whenever the program exits.

This code should show us the available nearby networks.

Here's the link to my code, (https://replit.com/@LarnelleAnkunda/WiFi-scanner)






