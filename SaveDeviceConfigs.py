import napalm
import json
import time
import os
from netmiko import ConnectHandler

dateTime = time.strftime("%m%d%y-%H%M%S")
netDevices = json.load(open('devices.json'))

for netDevice in netDevices:
    if netDevice['device_type'] == 'cisco_ios':
        driver = napalm.get_network_driver('ios')
        configStartPoint = 'startup'
        device = driver(hostname=netDevice['ip'], username=netDevice['username'],
                        password=netDevice['password'], timeout=10,
                        optional_args={'secret': netDevice['secret']})
    elif netDevice['device_type'] == 'fortinet':
        driver = napalm.get_network_driver('fortios')
        configStartPoint = 'running'
        device = driver(hostname=netDevice['ip'], username=netDevice['username'],
                        password=netDevice['password'], timeout=10)
    elif netDevice['device_type'] == 'cisco_asa':
        device = ConnectHandler(**netDevice)
    else:
        print('Unknown Device Type')
    # Begin Connection
    try:
        print('\nConnecting to ' + netDevice['ip'] + '...')
        if netDevice['device_type'] == 'cisco_asa':
            runningConfig = device.send_command('sh run')
            deviceName = device.send_command('sh hostname').strip('\n')
            device.disconnect()
        else:
            device.open()
            runningConfig = device.get_config()
            deviceName = device.get_facts()['hostname']
            device.close()
        print('Saving config: ' + deviceName)
        file = open("c:/users/"+os.getenv('username')+"/desktop/Configs/"+deviceName+"-"+netDevice['ip']+"-"+dateTime+".txt", "w")
        if netDevice['device_type'] == 'cisco_asa':
            file.write(runningConfig)
        else:
            file.write(runningConfig[configStartPoint])
        file.close()
    except:
        print('Failed to connect to ' + netDevice['ip'])
        