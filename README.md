# Network Scanner
This Python script allows you to scan a network and discover devices within a specified IP range. It uses Scapy, a powerful packet manipulation library, to send ARP request packets and capture responses from devices in the network. The script retrieves the IP address, MAC address, and hostname or vendor information for each discovered device.

## Prerequisites
- Python 3.x
- Required Python packages can be installed using the following command:
```commandline
pip install scapy requests
```

## Screenshots
- For Windows:
![](https://github.com/SaherMuhamed/network-scanner-tool/blob/master/screenshots/Screenshot%202023-12-27-windows.png)</br></br>
- For Linux:
![](https://github.com/SaherMuhamed/network-scanner-tool/blob/master/screenshots/Screenshot%202023-12-27-linux.png)

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
---------------------
Start time      : 27/12/2023 15:53:44 PM
Target subnet   : 192.168.152.1/24
---------------------

         IP            MAC Address      Hostname / Vendor  
-----------------------------------------------------------
   192.168.152.1    00:50:56:xx:xx:xx      VMware, Inc.    
   192.168.152.2    00:50:56:xx:xx:xx      VMware, Inc.    
  192.168.152.254   00:50:56:xx:xx:xx      VMware, Inc.    

---------------------
Summary         : 3 captured ARP Req/Res packets from 3 hosts 
Finished!
```
