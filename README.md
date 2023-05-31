# Network Scanner
This Python script allows you to scan a network and discover devices within a specified IP range. It uses Scapy, a powerful packet manipulation library, to send ARP request packets and capture responses from devices in the network. The script retrieves the IP address, MAC address, and hostname or vendor information for each discovered device.

### Prerequisites
- Python 3.x
- Required Python packages can be installed using the following command:
```commandline
pip install scapy requests prettytable progress
```

### Screenshot
- For Windows:
![screenshots/2023-05-31 21_26_16-Command Prompt.png](https://github.com/SaherMuhamed/network-scanner-python/blob/master/screenshots/2023-05-31%2021_26_16-Command%20Prompt.png)

### Usage
1. Clone the repository or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script with the following command:
```commandline
python3 network_device_scanner.py --range <IP_range> [--write <output_file>]
```
4. Replace <IP_range> with the IP range you want to scan, e.g., 192.168.1.0/24.
5. Optional: Specify the --write or -w flag followed by an <output_file> name to save the output to a text file.
6. The script will start scanning the network, displaying a progress bar and printing the discovered devices' information to the console.
7. If the --write or -w option is provided, the output table will be saved to the specified file.

### Output
The script generates a table displaying the following information for each discovered device:

- Device number
- IP address
- MAC address
- Hostname or vendor information (obtained from an API)

#### Example output:

```text
+-----+--------------+-------------------+-------------------------+
| No. | IP Address   | MAC Address       | Hostname / Vendor       |
+-----+--------------+-------------------+-------------------------+
| 0   | 192.168.1.1  | 00:0c:29:78:9c:44 | Cisco Systems           |
| 1   | 192.168.1.2  | 00:50:56:c0:00:08 | VMware                  |
| 2   | 192.168.1.10 | 00:0c:29:2b:55:0e | Dell                    |
+-----+--------------+-------------------+-------------------------+
```
