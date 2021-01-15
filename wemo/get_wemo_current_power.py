import http.client
from xml.etree import ElementTree
import paho.mqtt.client as mqtt
from datetime import datetime
import json

ipAddress = "10.112.10.133"
headers = {
    "Content-type": 'text/xml; charset="utf-8"',
    "SOAPACTION": '"urn:Belkin:service:insight:1#GetInsightParams"',
    "Content-Length": 271
}

data2 = '<?xml version="1.0" encoding="utf-8"?>' \
        '<s:Envelope ' \
        'xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"' \
        's:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">' \
        '<s:Body>' \
        '<u:GetInsightParams xmlns:u="urn:Belkin:service:insight:1"></u:GetInsightParams>' \
        '</s:Body>' \
        '</s:Envelope>'

conn = http.client.HTTPConnection(ipAddress, 49154)
conn.request("POST", "/upnp/control/insight1", data2, headers)
response = conn.getresponse()
resp_data = response.read()

if response.status == 200:
    conn.close()
    power_data_collections = ElementTree.fromstring(resp_data.decode()).find('.//InsightParams').text.split("|")

    client = mqtt.Client()
    client.username_pw_set(
        'xpimatpq',
        'r512yUWDQJO9'
    )
    client.connect('10.112.10.127', 50844, 2)

    payload = {
        'time': datetime.now().timestamp(),
        'current_power': power_data_collections[7],
    }
    client.publish('power_usage', json.dumps(payload))
elif response.status == 403:
    print("ERROR: 403 (FORBIDDEN)")
else:
    print("ERROR: " + str(response.status))