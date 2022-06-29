import write_text_file
import config
import socket
from datetime import datetime as timer


class CommunicationStatus:
    def __init__(self):
        self.write_file = write_text_file.WriteTextFile()
        self.write_path = config.WRITE_FILE_CONFIG.CONNECTION_LOG_PATH
        self.message = {}

    def create_log_message(self, status):
        current_time = timer.now().strftime("%H:%M:%S")
        self.message = {
            'brooker_ip_address': '192.168.1.59',
            'user_name': config.MQTT_CONFIG_CLIENT.DEVICE_TYPE,
            'client_ip_address': socket.gethostbyname(socket.gethostname()),
            'device_type': config.MQTT_CONFIG_CLIENT.DEVICE_NAME,
            'device_id': config.MQTT_CONFIG_CLIENT.DEVICE_IP,
            'timestamp': current_time,
            'status': status
        }

    def log_in_status(self, status):
        self.create_log_message(status)
        self.write_file.handle_write_file(self.write_path, 'ConnectionLog', 'a', self.message)


