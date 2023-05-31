import time
import requests
import scapy.all as scapy
from optparse import OptionParser
from prettytable import PrettyTable
from progress.bar import IncrementalBar


def get_argument():
    parser = OptionParser()
    parser.add_option("-r", "--range", dest="ip_range", help="Specify an IP Address range for your Subnet Mask. "
                                                             "Example: --range 192.168.1.1/24")
    parser.add_option("-w", "--write", dest="output_file", help="Specify the output file name to save the result (optional)")
    (options, arguments) = parser.parse_args()
    if not options.ip_range:
        parser.error("[-] Please specify an IP range, or type it correctly, ex: --range 192.168.1.1/24")

    return options


def scan_network(ip_address):
    # TODO 1: Create an ARP Request.
    arp_request = scapy.ARP(pdst=ip_address)
    # print(arp_request.summary())
    # print(arp_request.show())
    # scapy.ls(scapy.ARP())

    # TODO 2: Broadcast an ARP Packets to all Devices in the Network.
    broadcast_packets = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast_packets.summary())
    # scapy.ls(scapy.Ether())

    # TODO 3: Combining these 2 Packets together to Send.
    broadcast_arp_packets = broadcast_packets / arp_request
    # broadcast_arp_packets.show()

    # TODO 4: Start Send These Packets to all Devices.
    # answered_device, unanswered_device = scapy.srp(x=broadcast_arp_packets, timeout=3, verbose=False)
    answered_device = scapy.srp(x=broadcast_arp_packets, timeout=3, verbose=False)[0]
    # print(answered_device.summary())
    # print(unanswered_device.summary())

    return answered_device


device_no = 0
table = PrettyTable()
option = get_argument()

print("\nStart Scanning...")
answered_devices = scan_network(ip_address=option.ip_range)
bar = IncrementalBar(max=len(answered_devices), suffix='%(percent).1f%% - eta: %(eta)ds')

table.field_names = ["No.", "IP Address", "MAC Address", "Hostname / Vendor"]
for device in answered_devices:
    response = requests.get(url=f"https://api.macvendors.com/{device[1].hwsrc}", timeout=2)
    time.sleep(0.9)
    table.add_rows(
        [
            [device_no, device[1].psrc, device[1].hwsrc, response.text]
        ]
    )
    device_no += 1
    bar.next()

bar.finish()
print(f"{table}\nCompleted.")

if option.output_file:
    with open(option.output_file, "w") as f:
        f.write(str(table))
        print(f"[+] Output saved to {option.output_file}")
