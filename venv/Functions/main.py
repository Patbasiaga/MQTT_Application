import mqtt
import plc
import time
import message_handler


class Main:

    def __init__(self):
        self.mqtt_client = mqtt.MQTT()
        self.plc_client = plc.PLC()
        self.message_handler = message_handler.MessageHandler(self.mqtt_client)

    def start(self):
        while True:
            if self.mqtt_client.is_connected:
                if self.mqtt_client.message_received():
                    self.message_handler.is_heartbit_message()
                    self.message_handler.handle_ping_message()
                    self.message_handler.handle_mirror_message()
            # TODO DEBUG RECONNECTION - NOT WORKING PROPERLY - HANDLE RECONNECTING
            else:
                self.mqtt_client.connect_mqtt()
                time.sleep(1)


main = Main()

if __name__ == '__main__':
    main.start()


