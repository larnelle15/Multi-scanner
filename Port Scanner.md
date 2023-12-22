The port scanner I am going to create can work for both web applications and remote hosts and is meant to show the basic functionality of a port scanner. 

For this part, we need to use four libraries. These will be the pyfiglet, socket, sys and datetime libraries. I will implement alot of python socket programming to create this port scanner. The reason why i import the datetime libraries is because I want to be able to know what the current date and time is. The reason for that is I'm going to have the script tell us how long it took to execute. For it to be able to do that, it's going to need to know, here's where I started, here's when I ended. 

For my first function I will define my target and this involve translating my hostname to IPv4. I almost forgot the function for installing the datetime library will be:
(pip install datetime) 

Next I'll create a fancy port scanner that we'll see when my output is produced and this is the importance of the pyfiglet module.
Then I will create a for loop to scan ports between 1 and 70000, and make sure it returns an error indicator. 

Here is the output I got after running my code:

<img width="526" alt="Screen Shot 2023-12-22 at 3 51 07 PM" src="https://github.com/larnelle15/Multi-scanner/assets/139686202/b6f6c7fe-7aac-4a7a-8087-9868ff3cb945">



Here's a link to my code to see how it runs. (https://replit.com/@LarnelleAnkunda/EmbellishedAwkwardBackticks)
