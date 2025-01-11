import json
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

lambdaUrl = os.getenv('LAMBDA_FN_URL')
domain = os.getenv('DOMAIN')
secret = os.getenv('SECRET')
queryIntervalInSeconds = int(os.getenv('QUERY_INTERVAL_IN_SECONDS', '300'))
lastExternalIp = None
connection = FritzConnection(address=os.getenv('FRITZBOX_ADDRESS', 'fritz.box'))

while True:
    externalIp = connection.call_action('WANPPPConnection1', 'GetExternalIPAddress')['NewExternalIPAddress']

    if externalIp != lastExternalIp:
        lastExternalIp = externalIp

        response = requests.get(lambdaUrl, headers={'Content-Type': 'application/json'},
                                params={'domain': domain, 'secret': secret, 'ip': externalIp})

        logger.info(f"[STATUS {response.status_code}]: {response.content}")

    time.sleep(queryIntervalInSeconds)
