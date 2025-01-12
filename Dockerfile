FROM python:3.13.0-slim

RUN pip install fritzconnection
COPY update_dns_records.py /get_wan_ip.py

ENTRYPOINT [ "python", "/get_wan_ip.py" ]
