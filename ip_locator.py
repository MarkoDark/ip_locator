
import csv
import ipaddress
from collections import Counter


c_code = []
c_dict = {}
ip_counter = []

# Path needs to be adjusted
with open('/home/USER/DIRECTORY/ip-sorted.txt', 'r') as ipa_file:
    with open('/home/USER/DIRECTORY/ipIP2LOCATION-LITE-DB9.CSV', 'r') as csv_file:
        ipa_reader = ipa_file.readlines()
        csv_reader = csv.DictReader(csv_file)


        for line in csv_reader:
            for ipa in ipa_reader:
                start_ip = ipaddress.IPv4Address(int(line['start_ip']))
                end_ip = ipaddress.IPv4Address(int(line['end_ip']))
                cidr = ipaddress.summarize_address_range(ipaddress.IPv4Address(int(line['end_ip'])), ipaddress.IPv4Address(int(line['start_ip'])))
                # Get CIDR 
                for cidr_n in cidr:
                    cidr2 = cidr_n
                    break
                stripped_ip = ipaddress.IPv4Address(ipa.strip())
                #print(stripped_ip, cidr_n)
                if stripped_ip in cidr_n:
                    ##print(ipa.strip(), 'is in', cidr_n)

                    # IF YOU DON'T WANT THE CONSTANT OUTPUT
                    # DISABLE THIS PRINT STATEMENT BELOW!!!!
                    print(line['country_code'])
                    ip_counter.append(line['country_code'])
                    #print('DONE:', stripped_ip, '   CIDR:', cidr_n)
                    continue

                else:

                    continue

print(ip_counter)
print(Counter(ip_counter))




# Outcome

#['US', 'US', 'US', 'US', 'US', 'US', 'US', 'US', 'JP', 'JP', 'MY', 'TW', 'AU', 'AU', 'AU', 'AU', 'AU', 'HK', 'HK', 'HK', 'JP', 'JP', 'AU', 'AU', 'AU', 'AU', 'AU', 'AU', 'AU', 'AU', 'AU', 'AU', 'AU', 'TW', 'TW', 'TW', 'KR', 'KR', 'US', 'US', 'US', 'US', 'US', 'US', 'US']
#Counter({'AU': 16, 'US': 15, 'JP': 4, 'TW': 4, 'HK': 3, 'KR': 2, 'MY': 1})


