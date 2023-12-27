#!/usr/bin/env python3

import sys
import time
import datetime as dt
import requests
from prettytable import PrettyTable, HEADER, NONE
from argparse import ArgumentParser
import scapy.all as scapy

if sys.version_info < (3, 0):
    sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
    sys.stderr.write(
        "Please update and make sure you use the command python3 network_scanner.py -r <ip/24>\n\n")
    sys.exit(0)


def args():
    parser = ArgumentParser(description="Python script to perform active ARP ping scan", )
    parser.add_argument("-r", "--range", dest="ip_range", help="Specify an ip address range. Example: "
                                                               "--range 192.168.1.1/24", type=str)
    options = parser.parse_args()
    if not options.ip_range:
        parser.error(message="[-] Please specify valid ip address range, or type it correctly, ex: ---range "
                             "192.168.1.1/24")
    return options


def scan_network(ip_address, timeout=7):
    arp_request = scapy.ARP(pdst=ip_address)  # create an ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # broadcast an ARP packet to all devices in the network
    broadcast_arp_packets = broadcast / arp_request  # combine these 2 packets together to send

    answered, unanswered = scapy.srp(broadcast_arp_packets, timeout=timeout,
                                     verbose=False)  # send packets to all devices

    # extracting information from answered packets
    devices_list = []
    for sent_packet, received_packet in answered:
        # check if the packet contains an ARP layer
        if scapy.ARP in received_packet:
            device_info = {
                "ip": received_packet[scapy.ARP].psrc, 
                "mac": received_packet[scapy.Ether].src, 
                "packet_size": len(received_packet)
            }  # get the size of the packet
            devices_list.append(device_info)

    return devices_list


def get_details():
    print("\n---------------------")
    print("Start time      : " + str(dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")))
    print("Target subnet   : " + option.ip_range)
    print("---------------------\n")


option = args()
get_details()
x = PrettyTable(border=True, hrules=HEADER, vrules=NONE)
x.field_names = ["IP", "MAC Address", "Size", "Hostname / Vendor"]
devices = scan_network(ip_address=option.ip_range)

for device in devices:
    # response = requests.get(url="https://api.macvendors.com/" + device["mac"])  # old api call
    response = requests.get(url="https://www.macvendorlookup.com/api/v2/" + device["mac"], timeout=7)
    time.sleep(0.7)  # slow down the requests to api
    x.add_rows([[device["ip"], device["mac"], device["packet_size"], response.json()[0]["company"]]])
print(x.get_string(
    sortby="IP") + "\n")  # print table with ascending order ex. 192.168.1.1, 192.168.1.2, .., 192.168.1.254
print("---------------------")
print("Summary         : " + str(len(devices)) + " captured ARP Req/Res packets from " + str(
    len(devices)) + " hosts" + " \nFinished!\n")
