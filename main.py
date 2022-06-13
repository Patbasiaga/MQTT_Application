from mqtt import MQTT
from plc import PLC
import time
import message_handler


class main:
    def __init__(self):
        self.mqtt_client = MQTT()
        self.plc_client = PLC()

    #@staticmethod
    def start(self):
        message_handler.message_received(self.mqtt_client)
        if self.mqtt_client.is_connected:
            if message_handler.received_live_bit(self.mqtt_client):
                message_handler.send_live_bit(self.mqtt_client)

        else:
            self.mqtt_client.connect_mqtt()


gmain = main()


while True:
    gmain.start()


