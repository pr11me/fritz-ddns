# fritz-ddns

Provides Docker image in order to query the public IP of a FritzBox router for DDNS using the Python library
[fritzconnection](https://github.com/kbr/fritzconnection).

Although the FritzBox provides a DDNS service, it does not seem to work when the box is at the same time used as a
WireGuard client to a commercial VPN provider (Proton VPN in my case). This applies to both its DDNS setting for
custom DDNS providers and the resolution of the myfritz.net domain. In the former case, the log shows "DynDNS-Fehler:
Fehler bei der DNS-Auflösung des Domainnamens.", in the latter case "MyFRITZ! Fehler: Fehler bei der DNS-Auflösung
des MyFRITZ!-Namens".

The docker image provided here uses the queried IP to call
an [AWS Lambda function URL](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html), which changes 
an existing DNS record in Route53.

