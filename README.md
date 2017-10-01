# Network Automation
This repository contains a random collection of Python scripts that I've written to handle various network automation tasks, such as backing up router and switch configurations, pushing device configurations, or getting a list of firewall ACLs.

### SaveDeviceConfigs.py
This script will connect to every device listed in devices.json, get the running configuration, and save it to a text file with the device name and date/time. To add a device, simply create a JSON object for it within devices.json, and include the IP, credentials, and device type. The device type must match a netmiko device_type.