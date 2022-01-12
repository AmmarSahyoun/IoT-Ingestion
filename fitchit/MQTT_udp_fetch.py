
""" extract data from the IoT_MQTT_udp, transform to dataframe and save in a report """

import os, sys, logging, time, json, csv
import paho.mqtt.client as mqtt
from datetime import datetime


User = "assimilatus-grohuset-v3@ttn"
Password = "*****"
theRegion = "EU1"		

def saveToFile(json_file):
	end_device_ids = json_file["end_device_ids"]
	device_id = end_device_ids["device_id"]
	application_id = end_device_ids["application_ids"]["application_id"]
	received_at = json_file["received_at"]
	
	uplink_message = json_file["uplink_message"]
	f_port = uplink_message["f_port"]
	f_cnt = uplink_message["f_cnt"]
	frm_payload = uplink_message["frm_payload"]
	rssi = uplink_message["rx_metadata"][0]["rssi"]
	snr = uplink_message["rx_metadata"][0]["snr"]
	data_rate_index = uplink_message["settings"]["data_rate_index"]
	consumed_airtime = uplink_message["consumed_airtime"]
	
	# Daily log of uplinks
	now = datetime.now()
	pathNFile = now.strftime("%Y%m%d") + ".txt"
	print(pathNFile)
	if (not os.path.isfile(pathNFile)):
		with open(pathNFile, 'a', newline='') as tabFile:
			fw = csv.writer(tabFile, dialect='excel-tab')
			fw.writerow(["received_at", "application_id", "device_id", "f_port", "f_cnt", "frm_payload", "rssi", "snr", "data_rate_index", "consumed_airtime"])
	
	with open(pathNFile, 'a', newline='') as tabFile:
		fw = csv.writer(tabFile, dialect='excel-tab')
		fw.writerow([received_at, application_id, device_id, f_port, f_cnt, frm_payload, rssi, snr, data_rate_index, consumed_airtime])


