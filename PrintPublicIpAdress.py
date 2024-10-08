import os 

from fritzconnection import FritzConnection

with open('/run/secrets/user', 'r', encoding='utf-8') as userFile:
    user = userFile.read()
with open('/run/secrets/password', 'r', encoding='utf-8') as passwordFile:
    password = passwordFile.read()

address=os.getenv('FRITZBOX_ADDRESS', 'fritz.box')
file=os.getenv('PUBLIC_ADDRESS_FILE', '/out/public_address')

fc = FritzConnection(address=address, user=user, password=password)
external_ip = fc.call_action('WANIPConn1', 'GetExternalIPAddress')

with open(file, 'w', encoding='utf-8') as output:
    output.write(external_ip['NewExternalIPAddress'])

print(f"Public IP: {external_ip['NewExternalIPAddress']}")
