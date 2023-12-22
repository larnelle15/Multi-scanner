The port scanner I am going to create can work for both web applications and remote hosts and is meant to show the basic functionality of a port scanner. 

For this part, we need to use four libraries. These will be the pyfiglet, socket, sys and datetime libraries. I will implement alot of python socket programming to create this port scanner. The reason why i import the datetime libraries is because I want to be able to know what the current date and time is. The reason for that is I'm going to have the script tell us how long it took to execute. For it to be able to do that, it's going to need to know, here's where I started, here's when I ended. 

For my first function I will define my target and this involve translating my hostname to IPv4. I almost forgot the function for installing the datetime library will be:
(pip install datetime) 

Next I'll create a fancy port scanner that we'll see when my output is produced and this is the importance of the pyfiglet module.
Then I will create a for loop to scan ports between 1 and 70000, and make sure it returns an error indicator. 

Here is the output I got after running my code:
 ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
|  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
| |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
|  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
|_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
                                                                      

Invalid amount of Argument
--------------------------------------------------
Scanning Target: localhost
Scanning started at:2023-12-22 23:14:01.109814
--------------------------------------------------
Port 22 is open
Port 8283 is open
Port 33452 is open
Here's a link to my code(https://replit.com/@LarnelleAnkunda/EmbellishedAwkwardBackticks)
