import mqtt
import plc
import time
import mqtt_client
import message_handler_ping


class Main:
    def __init__(self):
        self.mqtt_client = mqtt_client.MqttHandler()
        self.plc_client = plc.PLC()

    def start(self):
        while True:
            if self.mqtt_client.is_connected:
                pass
            else:
                self.mqtt_client.connect_mqtt()
                time.sleep(1)


main = Main()

if __name__ == '__main__':
    main.start()

