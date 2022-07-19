import config
import json
import text_file_writer
import message_handler
import datetime
import time


class MessageHandlerPing:
    def __init__(self, client_mqtt):
        self.mqtt_client = client_mqtt
        self.message = {}
        self.message_json = ''
        self.text_file_writer = text_file_writer.TextFileWriter()
        self.path_to_write_file = config.WRITE_FILE_CONFIG.MESSAGE_LOG_PATH
        self.message_handler = message_handler.MessageHandler(self.mqtt_client)

    def is_valid_message(self):
        if (self.message_handler.is_message_for_this_device() and
                self.mqtt_client.converted_message["frame_type"] == "5"):
            return True

    def create_message(self):
        unix_ms_time = round(time.time()*1000)
        self.message = {
        #    'frame_type': '5',
        #    'device_type': config.MQTT_CONFIG_CLIENT.DEVICE_TYPE,
        #    'device_id': config.MQTT_CONFIG_CLIENT.DEVICE_ID,
        #    'device_name': config.MQTT_CONFIG_CLIENT.DEVICE_NAME,
        #    'device_IP': config.MQTT_CONFIG_SERVER.IP_ADDRESS,
        #    'timestamp': current_time,

                "EKF_vibe": {
                    "vibration_x": 0.11995743215084076,
                    "vibration_y": 0.11068499088287354,
                    "vibration_z": 0.11001553386449814
                },
        "GPS_sat": 10,
        "GPS_status": 6,
        "alt": 243070,
        "battery_current_consumed": 7643,
        "battery_remaining": 0,
        "current_battery": 2816,
        "current_waypoint": 9,
        "device_id": "00000000001",
        "device_type": 0,
        "frame_type": 1,
        "frame_version": 1,
        "ground_speed": 0,
        "head": 8240,
        "home_distance": 453.7839936835799,
        "lat": 50.6262851,
        "link_quality": 1,
        "load": 0,
        "lon": 21.9995284,
        "mode": 3,
        "onboard_control_sensors_health": 1399979183,
        "ping_time": 54.45,
        "radio_rssi": 255,
        "relative_alt": 99996,
        "system_status": 4,
        "time_boot_ms": 1598051,
        "timestamp": unix_ms_time,
        "voltage_battery": 12587
        }
        self.message_json = json.dumps(self.message)

    def send_message(self):
        print(self.message_json)
        self.mqtt_client.mqtt_publish("REAKTO/telemetry/drone1", self.message_json)

    def clear_message(self):
        self.message = {}
        self.message_json = ''

    def process_message(self):
       # if self.is_valid_message():
            self.clear_message()
            self.create_message()
            self.send_message()
          #  self.text_file_writer.handle_writing_to_file(self.path_to_write_file, 'ReceivedCorrectMessage',
             #                                            'a', self.message)
