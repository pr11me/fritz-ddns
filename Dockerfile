FROM python:3.13.0-slim

RUN pip install fritzconnection
COPY get_wan_ip.py /get_wan_ip.py

ENTRYPOINT [ "python", "/get_wan_ip.py" ]
