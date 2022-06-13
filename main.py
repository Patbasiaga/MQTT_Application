from mqtt import MQTT
from plc import PLC
import time
import message_handler


class main:
    def __init__(self):
        self.mqtt_client = MQTT()
        self.plc_client = PLC()

    def start(self):
        if message_handler.message_received():
            print(message_handler.correct_msg_received())


main = main()


while True:
    main.start()


