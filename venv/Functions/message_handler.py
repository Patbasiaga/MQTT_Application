import config
import json
import write_text_file
from datetime import datetime as timer


class MessageHandler:
    def __init__(self, brooker):
        self.brooker = brooker
        self.message = {}
        self.message_json = {}
        self.write_file = write_text_file.WriteTextFile()
        self.write_path = config.WRITE_FILE_CONFIG.MESSAGE_LOG_PATH

    # TODO ADD BROKEN MESSAGE HANDLING - I.E - JSON MESSAGE IS COMPLETED AND TARGETED THIS DEVICE
    #  BUT THERE IS A LACK OF ONE PARAMETER

    # Check If Message Target This Device
    def is_message_for_this_device(self):
        if (self.brooker.converted_message["device_type"] == config.MQTT_CONFIG_CLIENT.DEVICE_TYPE and
                self.brooker.converted_message["device_id"] == config.MQTT_CONFIG_CLIENT.DEVICE_ID and
                self.brooker.converted_message["device_name"] == config.MQTT_CONFIG_CLIENT.DEVICE_NAME and
                self.brooker.converted_message["device_IP"] == config.MQTT_CONFIG_CLIENT.DEVICE_IP):
            return True

    def write_json_received_message(self):
        with open('../../test_json.json', 'w') as file:
            file.write(self.brooker.json_message)

    def is_acknowledge_message(self):
        if self.brooker.ack_req:
            self.brooker.ack_req = False
            return False
        else:
            return True

    def clear_message(self):
        self.message = {}
        self.message_json = {}

    # HEARTBEAT Handling
    def is_heartbit_message(self):
        if (self.brooker.topic == 'HEARTBEAT' and self.is_message_for_this_device() and
                self.brooker.converted_message["frame_type"] == "0"):
            print("HEARTBEAT Received")

    # PING Handling
    def is_ping_message(self):
        if (self.brooker.topic == 'PING' and self.is_message_for_this_device() and
                self.brooker.converted_message["frame_type"] == "5"):
            return self.is_acknowledge_message()

    def create_ping_message(self):
        current_time = timer.now().strftime("%H:%M:%S")
        self.message = {
            'frame_type': '5',
            'device_type': config.MQTT_CONFIG_CLIENT.DEVICE_TYPE,
            'device_id': config.MQTT_CONFIG_CLIENT.DEVICE_ID,
            'device_name': config.MQTT_CONFIG_CLIENT.DEVICE_NAME,
            'device_IP': config.MQTT_CONFIG_CLIENT.DEVICE_IP,
            'timestamp': current_time,
        }
        self.message_json = json.dumps(self.message)

    def send_ping_message(self):
        self.brooker.ack_req = 1
        self.brooker.mqtt_publish("PING", self.message_json)

    def handle_ping_message(self):
        if self.is_ping_message():
            self.clear_message()
            self.create_ping_message()
            self.send_ping_message()
            self.write_file.handle_write_file(self.write_path, 'ReceivedCorrectMessage', 'a', self.message)

    # MIRROR Handling
    def is_mirror_message(self):
        if (self.brooker.topic == 'MIRROR' and self.is_message_for_this_device() and
                self.brooker.converted_message["frame_type"] == "6"):
            return self.is_acknowledge_message()

    def create_mirror_message(self):
        current_time = timer.now().strftime("%H:%M:%S")
        self.message = {
                        'frame_type': '6',
                        'device_type': config.MQTT_CONFIG_CLIENT.DEVICE_TYPE,
                        'device_id': config.MQTT_CONFIG_CLIENT.DEVICE_ID,
                        'device_name': config.MQTT_CONFIG_CLIENT.DEVICE_NAME,
                        'device_IP': config.MQTT_CONFIG_CLIENT.DEVICE_IP,
                        'timestamp': current_time,
                        'mirror': self.brooker.converted_message["mirror"]
                        }
        self.message_json = json.dumps(self.message)

    def send_mirror_message(self):
        self.brooker.ack_req = 1
        print(self.message_json)
        self.brooker.mqtt_publish("MIRROR", self.message_json)

    def handle_mirror_message(self):
        if self.is_mirror_message():
            self.clear_message()
            self.create_mirror_message()
            self.send_mirror_message()
            self.write_file.handle_write_file(self.write_path, 'ReceivedCorrectMessage', 'a', self.message)
