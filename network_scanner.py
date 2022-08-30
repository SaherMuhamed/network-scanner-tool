from tqdm import tqdm
import scapy.all as scapy
from optparse import OptionParser


def get_argument():
    parser = OptionParser()
    parser.add_option("-r", "--range", dest="range", help="Specify a range to search for")
    (options, arguments) = parser.parse_args()
    if not options.range:
        parser.error("[*] please specify an IP range to search for, use --help option for more info")
    else:
        return options


def scanning():
    option = get_argument()
    # TODO 1: Create an ARP Request.
    arp_request = scapy.ARP(pdst=option.range)
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
    # print(answered_list.summary())
    # print(unanswered_list.summary())
    return answered_list


def printing_answered_devices():
    devices = scanning()
    print("")
    print("_________________________________________")
    print(f"    IP\t\t\t   MAC Address")
    print("-----------------------------------------")
    for device in tqdm(devices, desc="Scanning...", ascii=False, ncols=75):
        print(f"{device[1].psrc}\t\t{device[1].hwsrc}")
    # print(devices.summary())
    print("Complete.")
    print("")


printing_answered_devices()
