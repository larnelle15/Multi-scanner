# Multi-Scanner
This was a personal research project that I presented for my Computer Science 2(Python) class at the end of the semester. Security risk is a big threat to people all over the world today. I gave an example of how businesses are the biggest target of network intrusions all over the world, and obviously its because of the important data that companies possess that could be used for blackmail or access to their income. In this project, I will talk about four mitigation strategies which would help reduce the risk down to an acceptable level and build three of them using python. The three I will be building are the network, wifi and port scanners and I will talk about creating a firewall in detail which is my fourth mitigation strategy. I will also create a firewall for wifi in particular using python. The scapy and socket libraries are going to be my best friends in this project but before I get into detail about the requirements of building these I want give descriptions on what a network, port, and wifi scanner are, as well as a firewall ofcourse.

# Network Scanner

<img width="724" alt="Screen Shot 2023-12-21 at 11 06 17 AM" src="https://github.com/larnelle15/Multi-scanner/assets/139686202/cfcfdb66-d922-4942-aba9-2c0f8a93d96c">

A network scanner is a software tool used for diagnostic and investigative purposes to find and categorize what devices are running on a network. Some of the most popular network scanning tools that people use are nessus, nexpose, Open VAS and Nmap which I have used in one of my previous projects labled Exploits where i practiced penetration testing using metasploitable. Mitigating security risks is easier when you can identify the security vulnerabilities and loopholes in the nodes of an entire network and that's where the network scanner comes in handy.

# WiFi Scanner

<img width="799" alt="Screen Shot 2023-12-21 at 11 24 03 AM" src="https://github.com/larnelle15/Multi-scanner/assets/139686202/cb1a0a00-44f0-4b04-8a11-0680278a1c7c">

A WiFi scanner is a tool that enables you to see the details related to nearby WiFi networks. The WiFi scanner above is called kismet and it is one of if not the best WiFi analyzer tool to use in linux OS, I also talked about it in my risk mitigation strategies file that you can find in this repository. A WiFi scanner can find out the following details about nearby networks:

SSID – The Service Set Identifier (SSID) is the name of the WiFi network. The SSID can be hidden, in which case a client who wants to connect must already know the name of the network. The name can also be sent through the beacons of the access points, enabling anyone who sees the network to attempt to gain access.

BSSID – The Basic Service Set Identifier (BSSID) is the access point’s MAC address.

Alias – This field will indicate if the network has an alias, and if so, will display it.

Channel – The channel that the wireless network is currently using for transmission is displayed on the channel field.

Band – The band field shows you what frequency is being employed by the WiFi network. You will usually find either 2.4 GHz or 5 GHz frequencies as they are the most commonly used bands.

Security – This essential field indicates what type of security is protecting a given network. If you are using a WiFi scanner to find networks that are easily accessible, you would like to find an open network. If WEP is the type of security being used, the network can be compromised fairly easily by hackers. WPA2 and WPA3 security provide enhanced protection and are very difficult to crack. You want your network to use this type of security to protect the data and devices which are connected to it.

Vendor – Here you will find the manufacturer for the WiFi router that is providing the network.

Mode – The mode field will tell you which wireless modes are supported by the router behind the network. A 2.4 GHz band can support the 802.11b, 802.11g, and 802.11n modes. The 5 GHz band Supports 802.11a, 802.11n, and 802.11ac.

Level (SNR) – This field reports the signal to noise ratio (SNR) of the queried network. It compares the level of the WiFi signal to the level of background noise.

Signal – The strength of the network signal is displayed in this field.

Signal % – This field shows the percentage of signal strength. The next three fields show the average, maximum, and minimum signal strengths.

Noise – Here you can see how much noise is impacting a particular network. The next field reports on the noise percentage.

Last seen – Here you will see how long it has been since your WiFi scanner could see a particular WiFi network.

For more information on WiFi scanners visit, (https://www.kismac-ng.org/wifi-scanner-for-macos/)

# Port Scanner

<img width="529" alt="Screen Shot 2023-12-21 at 11 38 11 AM" src="https://github.com/larnelle15/Multi-scanner/assets/139686202/3198678d-7d01-458f-b931-7669631a94b9">

A port scanner is a tool which can be used for determining which ports on a network are open and which ones could be receiving data. It is also used to probe a host or server to identify open ports. It is also valuable for testing network security and the strength of the system’s firewall. Due to this functionality, it is also a popular reconnaissance tool for attackers seeking a weak point of access to break into a computer. Ports vary in their services offered. They are numbered from 0 to 65535, but certain ranges are more frequently used. Ports 0 to 1023 are identified as the “well-known ports” or standard ports and have been assigned services by the Internet Assigned Numbers Authority (IANA). Some of the most prominent ports and their assigned services include:

Port 20 (UDP) — File Transfer Protocol (FTP) for data transfer
Port 22 (TCP) — Secure Shell (SSH) protocol for secure logins, FTP, and port forwarding
Port 23 (TCP) — Telnet protocol for unencrypted text commutations
Port 53 (UDP) — Domain Name System (DNS) translates names of all computers on internet-to-IP addresses
Port 80 (TCP) — World Wide Web HTTP
There are standard services offered on ports after 1023 as well and ports that, if open, indicate an infected system due to its popularity with some far-reaching Trojans and viruses.

The six types of port scanning techniques that can be used are the vanilla scan, ping scans, SYN scans, FTP Brounce scans, sweep scans and XMAS and FIN scans.

For more information on port scanners, you can visit (https://www.paloaltonetworks.com/cyberpedia/what-is-a-port-scan)

# Firewall

<img width="745" alt="Screen Shot 2023-12-21 at 12 13 32 PM" src="https://github.com/larnelle15/Multi-scanner/assets/139686202/977ce962-3c50-413e-a77d-2d1d3b78f6ac">

A firewall is a network security device that prevents unauthorized access to a network. It inspects incoming and outgoing traffic using a set of security rules to identify and block threats. A firewall can be physical hardware, digital software, software as a service (SaaS) or a virtual private cloud. I think we've all heard about firewalls before with examples of many action movies where they needed a hacker to break the firewalls at some super secure places like the pentagon or even the white house. I grew up watching these movies so up to now the topic always excites me. A firewall is one of if not the biggest mitigation strategy there is, and is capable of preventing unauthorized access to/from private networks. Here are the types of firewalls:
Network firewall
Web application firewall
Hardware-based
Software-based
Cloud-based
Personal computer (Windows, macOS) firewall
Mobile firewall
They are mostly categorized under two types – network-based and host-based.

For more information on firewalls, you can visit (https://geekflare.com/firewall-introduction/)

# Summary
Most of my research on these security measures are on the risk mitigation strategies.pdf file that I have placed in this repository and more of my projects involving cybersecurity are on my github profile named Exploits, DIY-Malware, and password crack-a-thon. Now that everything I will be dealing with has been described, let's begin!
