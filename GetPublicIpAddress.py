import os 
import time

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
intervall=int(os.getenv('INTERVALL', '300'))

last_external_ip = None

while True:
    fc = FritzConnection(address=address, user=user, password=password)
    external_ip = fc.call_action('WANIPConn1', 'GetExternalIPAddress')['NewExternalIPAddress']

    if external_ip != last_external_ip:
        last_external_ip = external_ip
        with open(file, 'w', encoding='utf-8') as output:
            output.write(f"{outputPrefix}{external_ip}")

        print(f"Public IP: {external_ip}")

    time.sleep(intervall)
