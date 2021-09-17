#!/usr/bin/env/ python3


# Sort them

ip_unsorted = []

# Path needs to be adjusted

with open('/home/USER/DIRECTORY/ip-addresses.txt', 'r') as file:
    for ip in file:
        stripped_ip = ip.strip()
        ip_unsorted.append(stripped_ip)



print(len(ip_unsorted))


not_null_ip_unosrted = []


for ip_addr in ip_unsorted:
    if len(ip_addr) == 0:
        continue
    not_null_ip_unosrted.append(ip_addr)

print(len(not_null_ip_unosrted))


not_null_ip_unosrted.sort()
sorted_ip = not_null_ip_unosrted
# print(sorted_ip)

# Path needs to be adjusted
with open('/home/USER/DIRECTORY/ip-sorted.txt', 'w') as ip_file:
    for ip_address in sorted_ip:
        ip_file.write('%s\n'  % ip_address)



