# IP Locator

This program can determine to which country does an IP address belongs.

We can approximate one’s location based on the IP address because blocks of IP addresses get allocated to a country, ISPs (internet service providers) either buy or lease a certain number of IP addresses from a registry to distribute them to users.

The program takes an IP address and tries to find the IP range it belongs to. When it finds the range, the country code gets recorded, and a process starts all over again with a new IP address.


## The structure and the order of execution

Here is a nice visual representation of each file, its duty, and its output type. This is also the order you want to follow.

<pre><code>

<b>0. DESCRIPTION</b>
|
+---> NAME OF THE SCRIPT
|
|
+------> OUTPUT TYPE



<b>1. Sort IPs in the ascending order</b>
|
+---> sort_ip_asc.py
|
|
+------> ip-sorted.txt



<b>2. Make an IP range</b>
|
+---> ip_range.py
|
|
+------> REDIRECT THE OUTPUT



<b>3. Find out country code based on the IP address</b>
|
+---> ip_locator.py
|
|
+------> REDIRECT THE OUTPUT 

</pre></code>

# Additional files

If you don't want to download the database, or if you immediately want to start examining IP addresses, then you can take the CSV file I created (*asc_cc_cidr.csv*) and run "*ip_locator.py*"
Set paths correctly!


# Heads Up

1. The entire process may take some time because Python can't work with more than one CPU core at a time.

2. Paths within the code itself must be properly set. As a default, I left it as *“/home/USER/DIRECTORY/”*.
If you want to run it on Windows you will have to ensure no SyntaxErrors get raised when it’s trying to read the path. Write *”C:/Users/USER/Desktop/”* instead of *“C:\Users\USER\Desktop\\"* and you will be golden.



--------

Tested on:  Ubuntu 20.04.1 || 
            Windows 10

Python 3.8.10

Modified:   16.9.2021