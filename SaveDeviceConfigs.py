import napalm
import json
import time

devices = json.load(open('devices.json'))

#iosDevices = ['10.199.1.74','10.199.1.36','10.199.1.37','199.120.209.2','199.120.209.3']
#fortiosDevices = ['10.199.1.41']

dateTime = time.strftime("%m%d%y-%H%M%S")

for iosDevice in iosDevices:
    driver = napalm.get_network_driver('ios')
    device = driver(hostname=iosDevice, username='network', password='2GssHAxe$$', timeout=10, optional_args={'secret':'4enableAxe$$'})
    try:
        print('Connecting to ' + iosDevice)
        device.open()
        runningConfig = device.get_config()
        deviceName = device.get_facts()['hostname']
        device.close()
        print('Saving config: ' + deviceName)
        file = open("c:/users/cfonseca/desktop/"+deviceName+"-"+dateTime+".txt", "w")
        file.write(runningConfig['startup'])
        file.close()
    except:
        print('Failed to connect to ' + iosDevice)

for fortiosDevice in fortiosDevices:
    driver = napalm.get_network_driver('fortios')
    device = driver(hostname=fortiosDevice, username='admin', password='l0gm3!n2FortiG@t3', timeout=10)
    try:
        print('Connecting to ' + fortiosDevice)
        device.open()
        runningConfig = device.get_config()
        deviceName = device.get_facts()['hostname']
        device.close()
        print('Saving config: ' + deviceName)
        file = open("c:/users/cfonseca/desktop/"+deviceName+"-"+dateTime+".txt", "w")
        file.write(runningConfig['running'])
        file.close()
    except:
        print('Failed to connect to' + fortiosDevice)

# https://napalm.readthedocs.io/en/latest/base.html
