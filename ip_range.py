import ipaddress
import csv

# Path needs to be adjusted
with open('/home/USER/DIRECTORY/IP2LOCATION-LITE-DB9.CSV', 'r') as csv_file:

    csv_reader = csv.DictReader(csv_file)
    
    for line in csv_reader:
        cidr = ipaddress.summarize_address_range(ipaddress.IPv4Address(int(line['end_ip'])), ipaddress.IPv4Address(int(line['start_ip'])))

        for cidr_num in cidr:
            print(line['country_code'], cidr_num)

# Sample output

# AU 1.136.17.0/24
# AU 1.136.18.0/23


