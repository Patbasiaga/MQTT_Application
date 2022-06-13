from plc import PLC
from mqtt import MQTT
from config import MQTT_CONFIG
import time


def message_received(brooker):
    if brooker.received:
        brooker.received = False
        return True


def correct_msg_received(brooker):
    try:
        MQTT_CONFIG.TOPICS.index(brooker.topic)
        return True
    except ValueError:
        return False


#Live Bit Handling
def received_live_bit(brooker):
    if brooker.topic == 'Live_Bit' and brooker.converted_message == 'ON':
        return True


def send_live_bit(brooker):
    time.sleep(1)
    brooker.mqtt_publish("Live_Bit", "OFF")
    brooker.live_bit = 0


def received_request_land():
    MQTT.mqtt_publish("HUB_001/Land", "False")


def received_allowed_positioning():
    MQTT.mqtt_publish("HUB_001/Positioning", "False")


def send_allowed_land():
    MQTT.mqtt_publish("HUB_001/Land", "True")


def send_allowed_start():
    MQTT.mqtt_publish("HUB_001/Start", "True")
