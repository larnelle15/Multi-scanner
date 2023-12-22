The port scanner I am going to create can work for both web applications and remote hosts and is meant to show the basic functionality of a port scanner. 

For this part, we need to use four libraries. These will be the pyfiglet, socket, sys and datetime libraries. I will implement alot of python socket programming to create this port scanner. The reason why i import the datetime libraries is because I want to be able to know what the current date and time is. The reason for that is I'm going to have the script tell us how long it took to execute. For it to be able to do that, it's going to need to know, here's where I started, here's when I ended. 

For my first function I will define my target and this involve translating my hostname to IPv4. I almost forgot the function for installing the datetime library will be:
(pip install datetime) 

Next I'll create a fancy port scanner that we'll see when my output is produced and this is the importance of the pyfiglet module.

