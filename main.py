from mqtt import MQTT
from plc import PLC
import time
import message_handler


class Main:

    def __init__(self):
        self.mqtt_client = MQTT()
        self.plc_client = PLC()

    def start(self):
        if self.mqtt_client.is_connected:
            if self.mqtt_client.message_received():
                message_handler.live_bit_handle(self.mqtt_client)

        else:
            self.mqtt_client.connect_mqtt()
            time.sleep(1)


main = Main()


while True:
    main.start()


