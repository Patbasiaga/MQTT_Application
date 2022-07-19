from mqtt import MQTT
import json
import message_handler_ping
import message_handler_mirror
import message_handler_heartbeat


class MqttHandler(MQTT):
    def __init__(self):
        super().__init__()
        self.message_handler_ping = message_handler_ping.MessageHandlerPing(self)
        self.message_handler_mirror = message_handler_mirror.MessageHandlerMirror(self)
        self.message_handler_heartbeat = message_handler_heartbeat.MessageHandlerHeartbeat(self)

    def handle_the_right_topic(self):
        #if self.topic == "PING":
        self.message_handler_ping.process_message()

       # if self.topic == "MIRROR":
       #     self.message_handler_mirror.process_message()

        #if self.topic == "HEARTBEAT":
        #    self.message_handler_heartbeat.is_valid_message()
