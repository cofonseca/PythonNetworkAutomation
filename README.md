# Network Automation
This repository contains a random collection of Python scripts that I've written to handle various network automation tasks, such as backing up router and switch configurations, pushing device configurations, or getting a list of firewall ACLs.

### SaveDeviceConfigs.py
This script will connect to every device listed in devices.json, get the running configuration, and save it to a text file with the device name and date/time. To add a device, simply create a JSON object for it within devices.json, and include the IP, credentials, and device type. The device type must match a netmiko device_type.

### CompareDeviceConfigs.py
This script will connect to a device, and compare its running configuration to a previous configuration in the form of a text file. The script takes two arguments: 
1. The IP Address of the device to connect to and compare
2. The full path to the config .txt file to compare against

Any differences between the live configuration and the previous configuration will be printed to the console. If the live config and previous config match, the script will not return anything.
```
CompareDeviceConfigs.py 10.0.1.1 C:\Configs\R1-10.0.1.1.txt
```

### Contributing and Upcoming Features
Although this is primarily a private project, I'm certainly open to learning, and always welcome suggestions or ideas on how to implement new features. Some of my current ideas include:
- Parallel processing and/or multithreading
- Securing login credentials in devices.json
- Reading from and writing to a database
- A Flask-based front-end