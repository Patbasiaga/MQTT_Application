import config
import json
import text_file_writer
from datetime import datetime as timer


class MessageHandler:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client
        self.message = {}
        self.message_json = ''

    # Check If Message Target This Device
    def is_message_for_this_device(self):
        if (self.mqtt_client.converted_message["device_type"] == config.MQTT_CONFIG_CLIENT.DEVICE_TYPE and
                self.mqtt_client.converted_message["device_id"] == config.MQTT_CONFIG_CLIENT.DEVICE_ID and
                self.mqtt_client.converted_message["device_name"] == config.MQTT_CONFIG_CLIENT.DEVICE_NAME and
                self.mqtt_client.converted_message["device_IP"] == config.MQTT_CONFIG_CLIENT.DEVICE_IP):
            return True

    def write_json_message_to_file(self):
        with open('../../test_json.json', 'w') as file:
            file.write(self.mqtt_client.json_message)
