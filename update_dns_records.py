import logging
import os
import time

import requests
from fritzconnection import FritzConnection

logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)

lambda_url = os.getenv('LAMBDA_FN_URL')
domain = os.getenv('DOMAIN')
secret = os.getenv('SECRET')
query_interval_in_seconds = int(os.getenv('QUERY_INTERVAL_IN_SECONDS', '300'))
last_external_ip = None
connection = FritzConnection(address=os.getenv('FRITZBOX_ADDRESS', 'fritz.box'))

while True:
    external_ip = connection.call_action('WANPPPConnection1', 'GetExternalIPAddress')['NewExternalIPAddress']

    if external_ip != last_external_ip:
        last_external_ip = external_ip

        response = requests.get(lambda_url, params={'domain': domain, 'secret': secret, 'ip': external_ip})

        logger.info(f"[STATUS {response.status_code}]: {response.content}")

    time.sleep(query_interval_in_seconds)
