#!/usr/bin/env python3

import sys
import time
import requests
from argparse import ArgumentParser
import scapy.all as scapy

if sys.version_info < (3, 0):
    sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
    sys.stderr.write(
        "Please update and make sure you use the command python3 network_scanner.py -r <ip/24>\n\n")
    sys.exit(0)


def args():
    parser = ArgumentParser()
    parser.add_argument("-r", "--range", dest="ip_range", help="Specify an ip address range. Example: "
                                                               "--range 192.168.1.1/24")
    options = parser.parse_args()
    if not options.ip_range:
        parser.error(message="[-] Please specify valid ip address range, or type it correctly, ex: ---range "
                             "192.168.1.1/24")
    return options


def scan_network(ip_address):
    arp_request = scapy.ARP(pdst=ip_address)  # create an ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # broadcast an ARP packets to all devices in the network
    broadcast_arp_packets = broadcast / arp_request  # combining these 2 packets together to send

    ans, unans = scapy.srp(broadcast_arp_packets, timeout=2, verbose=False)  # send packets to all devices
    return ans[0]  # return answered devices only


option = args()
devices = scan_network(ip_address=option.ip_range)

print("\n___________________________________________________________________")
print("    IP\t\t   MAC Address\t\t     Hostname / Vendor")
print("-------------------------------------------------------------------")
for device in devices:
    response = requests.get(url="https://api.macvendors.com/" + device[1].hwsrc)
    time.sleep(1)
    print(device[1].psrc + "\t" + device[1].hwsrc + "\t" + response.text)
