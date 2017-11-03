import time
import os
import sys
import json
import napalm

ip_address = sys.argv[1]
configFile = sys.argv[2]

if len(sys.argv) != 3:
    print("Usage: compareDeviceConfigs.py <IP Address> <Config.txt>")

netDevices = json.load(open('devices.json'))
for netDevice in netDevices:
    if netDevice['ip_address'] == ip_address:
        if netDevice['device_type'] == 'cisco_ios':
            driver = napalm.get_network_driver('ios')
            device = driver(hostname=netDevice['ip_address'], username=netDevice['username'],
                            password=netDevice['password'], timeout=10,
                            optional_args={'secret': netDevice['secret']})
        elif netDevice['device_type'] == 'fortinet':
            driver = napalm.get_network_driver('fortios')
            device = driver(hostname=netDevice['ip_address'], username=netDevice['username'],
                            password=netDevice['password'], timeout=10)
        else:
            print('Unknown Device Type')
        # Begin Connection
        try:
            print('\nConnecting to ' + netDevice['ip_address'])
            device.open()
            print('Loading Configuration...')
            device.load_merge_candidate(configFile)
            print('Comparing Configuration...')
            diffs = device.compare_config()
            if len(diffs) > 0:
                print('Differences:')
                print(diffs)
            device.discard_config()
            device.close()
        except:
            print('Failed to connect to ' + netDevice['ip_address'])

# https://napalm.readthedocs.io/en/latest/base.html
