from netmiko import ConnectHandler

SW2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': 'korir',
    'password': 'victorsecrets',
}

SW3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.83',
    'username': 'korir',
    'password': 'victorsecrets',
}

SW4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.84',
    'username': 'korir',
    'password': 'victorsecrets',
}

SW5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.85',
    'username': 'korir',
    'password': 'victorsecrets',
}

SW6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.86',
    'username': 'korir',
    'password': 'victorsecrets',
}

with open('cisc_cmds') as f:
    lines = f.read().splitlines()
print (lines)

devices = [SW4, SW5, SW6]

for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print (output)


with open('core_cmds') as f:
    lines = f.read().splitlines()
print (lines)


devices = [SW6, SW5, SW4, SW3, SW2]

for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print (output)

