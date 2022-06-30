import message_handler


class MessageHandlerHeartbeat:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client
        self.message_handler = message_handler.MessageHandler(self.mqtt_client)
        # HEARTBEAT Handling

    def is_valid_message(self):
        if(self.mqtt_client.topic == 'HEARTBEAT' and self.message_handler.is_message_for_this_device() and
                self.mqtt_client.converted_message["frame_type"] == "0"):
            print("HEARTBEAT Received")
