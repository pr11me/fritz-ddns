FROM python:3.13.0-slim

RUN pip install fritzconnection
COPY update_dns_records.py /update_dns_records.py

ENTRYPOINT [ "python", "/update_dns_records.py" ]
