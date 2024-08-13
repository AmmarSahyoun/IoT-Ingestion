""" This piece of code is a part of IoT project that configured to fetch data from
 Dragino LHT65 that is a temperature and Humidity sensor. """

import os, requests, json, csv
from datetime import datetime


theApplication = "assimilatus-grohuset-v3"
theAPIKey = "******"
theRegion = "EU1"
url="https://eu1.cloud.thethings.network/api/v3/as/applications/assimilatus-grohuset-v3/packages/storage/uplink_message?order=received_at&type=uplink_message&limit=4&after=2022-01-06T19:00:00Z"

headers = {'Accept': 'text/event-stream', 'Authorization': 'Bearer ' + theAPIKey}

r = requests.get(url, headers=headers)

to_json = "{\"data\": [" + r.text.replace("\n\n", ",")[:-1] + "]}"
json_file = json.loads(to_json)
uplinks = json_file['data']

now = datetime.now()
filename = "Assimilatus-" + theApplication + "-" + now.strftime("%Y%m%d%H%M%S") + ".txt"

def get_report():
    if (not os.path.isfile(filename)):
        with open(filename, 'a', newline='') as tabFile:
            fw = csv.writer(tabFile, dialect='excel-tab')
            fw.writerow(["sensor", "temp", "battery", "humidity", "rssi", "received_at"])

    for data in uplinks:
        result = data["result"]
        device_id = result["end_device_ids"]['device_id']
        received_at = result["received_at"]
        received_at = received_at.split('.')[0]
        uplink_message = result["uplink_message"]
        rssi = uplink_message["rx_metadata"][0]["rssi"]
        battery = uplink_message['decoded_payload']['BatV']
        humidity = uplink_message['decoded_payload']['Hum_SHT']
        temperature = uplink_message['decoded_payload']['TempC_SHT']
        with open(filename, 'a', newline='') as output:
            output = csv.writer(output, dialect='excel-tab')
            output.writerow([device_id, temperature, battery, humidity, rssi, received_at])


if __name__ == '__main__':
    get_report()