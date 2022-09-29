import time
import requests
import scapy.all as scapy
from prettytable import PrettyTable
from optparse import OptionParser


def get_argument():
    parser = OptionParser()
    parser.add_option("-r", "--range", dest="range", help="Specify a range to search for")
    (options, arguments) = parser.parse_args()
    if not options.range:
        parser.error("[*] please specify an IP range to search for, use --help option for more info")
    else:
        return options


def get_mac_vendor(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    time.sleep(1)
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.content.decode("UTF-8")


def scanning(ip_address):
    # TODO 1: Create an ARP Request.
    arp_request = scapy.ARP(pdst=ip_address)
    # print(arp_request.show())
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())

    # TODO 2: Broadcast an ARP Packets to all Devices in the Subnet Mask.
    broadcast_packets = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast_packets.summary())
    # scapy.ls(scapy.Ether())

    # TODO 3: Combining these 2 Packets Together to Send.
    broadcast_arp_packets = broadcast_packets / arp_request
    # print(broadcast_arp_packets.summary())

    # TODO 4: Send Packets & Receive Responses.
    answered_list, unanswered_list = scapy.srp(broadcast_arp_packets, timeout=3, verbose=False)
    time.sleep(1)
    # print(answered_list.summary())
    # print(unanswered_list.summary())

    return answered_list


option = get_argument()
devices = scanning(ip_address=option.range)
table = PrettyTable()
table.field_names = ["ID", "IPs", "MAC Address", "Vendor / Hostname"]
device_id = 0
for device in devices:
    table.add_rows(
        [
            [device_id, device[1].psrc, device[1].hwsrc, get_mac_vendor(mac_address=device[1].hwsrc)]
        ]
    )
    device_id += 1
print(table)
print("Complete.")
