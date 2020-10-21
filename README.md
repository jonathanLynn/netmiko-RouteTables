# NetMiko-RouteTables
Keep a historical record of your Cisco Device's Routing Table. Great during Operational/Project Work when you want to retrospectively see how traffic was being routed from a given device.

## Setup And Installation
Ensure you install NetMiko by using the below command:

```
pip install netmiko
```

This script has been tested on Python 2.6 and Python 3.6 - It is recommended to use Python3 for this script and future iterations of it.

## Using The Script
The script simply probes the Cisco Device for its route table using the show command "show ip route" and then saves the output into a file located in the same directory as the script with the name corrolating to the date and time of when the script was executed.

### Running the Script

```
python3 routetables.py
```
