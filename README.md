# Network Scanner
This Python script allows you to scan a network and discover devices within a specified IP range. It uses Scapy, a powerful packet manipulation library, to send ARP request packets and capture responses from devices in the network. The script retrieves the IP address, MAC address, and hostname or vendor information for each discovered device.

## Prerequisites
- Python 3.x
- Required Python packages can be installed using the following command:
```commandline
pip install scapy requests
```

## Screenshot
- For Windows:
![screenshots/windows.png](https://github.com/SaherMuhamed/network-scanner-python/blob/master/screenshots/windows.png)</br></br>
- For Linux:
![screenshots/Screenshot from 2023-09-17 14-26-10.png]([https://github.com/SaherMuhamed/network-scanner-python/blob/master/screenshots/linux.gif](https://github.com/SaherMuhamed/network-scanner-tool/blob/master/screenshots/Screenshot%20from%202023-09-17%2014-26-10.png)

## Usage
1. Clone the repository or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script with the following command:
```commandline
python3 network_device_scanner.py --range <IP_range>
```
4. Replace <IP_range> with the IP range you want to scan, e.g., 192.168.1.1/24.

## Output
The script generates a table displaying the following information for each discovered device:

- IP address
- MAC address
- Hostname or vendor information (obtained from an API)

## Example output:

```text
___________________________________________________________________
    IP		   MAC Address		     Hostname / Vendor
-------------------------------------------------------------------
192.168.1.3	14:eb:b6:xx:xx:xx	TP-Link Corporation Limited
192.168.1.1	8c:0d:76:xx:xx:xx	HUAWEI TECHNOLOGIES CO.,LTD
```
