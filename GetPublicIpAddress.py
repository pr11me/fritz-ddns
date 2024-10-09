import os 

from fritzconnection import FritzConnection

userFile=os.getenv('FRITZBOX_USER_FILE', '/run/secrets/user')
passwordFile=os.getenv('FRITZBOX_PASSWORD_FILE', '/run/secrets/password')

with open(userFile, 'r', encoding='utf-8') as userFile:
    user = userFile.read()
with open(passwordFile, 'r', encoding='utf-8') as passwordFile:
    password = passwordFile.read()

address=os.getenv('FRITZBOX_ADDRESS', 'fritz.box')
file=os.getenv('PUBLIC_ADDRESS_FILE', '/out/public_address')
outputPrefix=os.getenv('OUTPUT_PREFIX', '')

fc = FritzConnection(address=address, user=user, password=password)
external_ip = fc.call_action('WANIPConn1', 'GetExternalIPAddress')

with open(file, 'w', encoding='utf-8') as output:
    output.write(f"{outputPrefix}{external_ip['NewExternalIPAddress']}")

print(f"Public IP: {external_ip['NewExternalIPAddress']}")
