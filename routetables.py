from netmiko import ConnectHandler
from getpass import getpass
import datetime

class deviceOutput:
        '''This Class outlines the data that gets taken from the Network Device and saved into an output file'''
        def __init__(self, string):
                self.string = string

        def createNewFile(self):
                '''This Function checks the date and time and appends this to the filename during creation'''
                f = open(str(datetime.datetime.now()) + ".txt", "a")
                f.write(self.string)
                f.close()

networkDevice1 = {
    "device_type": "cisco_ios",
    "host": "{IP ADDRESS HERE}",
    "username": "{USERNAME}",
    "password": getpass(),
}

# Show command that we execute.
command = "show ip route"

with ConnectHandler(**networkDevice1) as net_connect:
    output = net_connect.send_command(command)

# Automatically cleans-up the output so that only the show output is returned

outputFromDevice = deviceOutput(output)

print("Saving Output now")
outputFromDevice.createNewFile()
print()
print("Complete")
