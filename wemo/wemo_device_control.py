import http.client

ipAddress = "10.112.10.133"


def turn_off_device(value=0):
    data = '' \
           '<?xml version="1.0" encoding="utf-8"?>' \
           '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" ' \
           's:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">' \
           '<s:Body><u:SetBinaryState xmlns:u="urn:Belkin:service:basicevent:1">' \
           '<BinaryState>' + str(value) + \
           '</BinaryState>' \
           '</u:SetBinaryState>' \
           '</s:Body>' \
           '</s:Envelope>'

    headers = {
        "Content-type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:Belkin:service:basicevent:1#SetBinaryState"',
        "Content-Length": len(data)
    }

    conn = http.client.HTTPConnection(ipAddress, 49154)
    conn.request(
        "POST",
        "/upnp/control/basicevent1",
        data,
        headers
    )
    response = conn.getresponse()
    if response.status == 200:
        conn.close()
        print("SUCCESS!")
    elif response.status == 403:
        print("ERROR: 403 (FORBIDDEN)")
    else:
        print("ERROR: " + str(response.status))


def turn_on_device(value=1):
    data = '' \
           '<?xml version="1.0" encoding="utf-8"?>' \
           '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" ' \
           's:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">' \
           '<s:Body><u:SetBinaryState xmlns:u="urn:Belkin:service:basicevent:1">' \
           '<BinaryState>' + str(value) + \
           '</BinaryState>' \
           '</u:SetBinaryState>' \
           '</s:Body>' \
           '</s:Envelope>'

    headers = {
        "Content-type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:Belkin:service:basicevent:1#SetBinaryState"',
        "Content-Length": len(data)
    }

    conn = http.client.HTTPConnection(ipAddress, 49154)
    conn.request(
        "POST",
        "/upnp/control/basicevent1",
        data,
        headers
    )
    response = conn.getresponse()
    if response.status == 200:
        conn.close()
        print("SUCCESS!")
    elif response.status == 403:
        print("ERROR: 403 (FORBIDDEN)")
    else:
        print("ERROR: " + str(response.status))


turn_on_device()
