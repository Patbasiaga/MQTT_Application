import time


# Live Bit Handling
def received_live_bit(brooker):
    if brooker.topic == 'Live_Bit' and brooker.converted_message == 'ON':
        return True


def send_live_bit(brooker):
    brooker.mqtt_publish("Live_Bit", "OFF")
    brooker.live_bit = 0


def live_bit_handle(brooker):
    if received_live_bit(brooker):
        time.sleep(1)
        send_live_bit(brooker)


def received_request_land():
    MQTT.mqtt_publish("HUB_001/Land", "False")


def received_allowed_positioning():
    MQTT.mqtt_publish("HUB_001/Positioning", "False")


def send_allowed_land():
    MQTT.mqtt_publish("HUB_001/Land", "True")


def send_allowed_start():
    MQTT.mqtt_publish("HUB_001/Start", "True")
