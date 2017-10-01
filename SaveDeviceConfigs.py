import napalm
import json
import time
import os

dateTime = time.strftime("%m%d%y-%H%M%S")
netDevices = json.load(open('devices.json'))

for netDevice in netDevices:
    if netDevice['device_type'] == 'cisco_ios':
        driver = napalm.get_network_driver('ios')
        configStartPoint = 'startup'
        device = driver(hostname=netDevice['ip_address'], username=netDevice['username'], password=netDevice['password'], timeout=10, optional_args={'secret': netDevice['secret']})
    elif netDevice['device_type'] == 'fortinet':
        driver = napalm.get_network_driver('fortios')
        configStartPoint = 'running'
        device = driver(hostname=netDevice['ip_address'], username=netDevice['username'], password=netDevice['password'], timeout=10)
    else:
        print('Unknown Device Type')
    # Begin Connection
    try:
        print('Connecting to ' + netDevice['ip_address'])
        device.open()
        runningConfig = device.get_config()
        deviceName = device.get_facts()['hostname']
        device.close()
        print('Saving config: ' + deviceName)
        file = open("c:/users/"+os.getenv('username')+"/desktop/"+deviceName+"-"+netDevice['ip_address']+"-"+dateTime+".txt", "w")
        file.write(runningConfig[configStartPoint])
        file.close()
    except:
        print('Failed to connect to ' + netDevice['ip_address'])

# https://napalm.readthedocs.io/en/latest/base.html
