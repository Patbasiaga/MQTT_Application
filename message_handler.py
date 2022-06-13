from plc import PLC
from mqtt import MQTT
from config import MQTT_CONFIG
import time

mqtt_client = MQTT()


def message_received():
    if mqtt_client.is_connected:
        if mqtt_client.received:
            mqtt_client.received = False
            return True
    else:
        mqtt_client.connect_mqtt()
        time.sleep(1)
        return False


def correct_msg_received():
    try:
        MQTT_CONFIG.TOPICS.index(mqtt_client.topic)
        return True
    except ValueError:
        return False




def received_request_land():
    MQTT.mqtt_publish("HUB_001/Land", "False")


def received_allowed_positioning():
    MQTT.mqtt_publish("HUB_001/Positioning", "False")


def send_allowed_land():
    MQTT.mqtt_publish("HUB_001/Land", "True")


def send_allowed_start():
    MQTT.mqtt_publish("HUB_001/Start", "True")
#            main.client.topic == "stat/SwitchKuchnia/POWER1" or "stat/SwitchProba2/POWER2") and client.converted_message == "OFF" and kuchniaSwitchStatus == "ON":
#        client.mqtt_publish("cmnd/SwitchKuchnia/POWER1", 'OFF')
 ##      client.converted_message = "None"
   #     kuchniaSwitchStatus = "OFF"

    #if (
     #       client.topic == "stat/SwitchKuchnia/POWER1" or "stat/SwitchProba2/POWER2") and client.converted_message == "ON" and kuchniaSwitchStatus == "OFF":
      #  client.mqtt_publish("cmnd/SwitchKuchnia/POWER1", 'ON')
       # client.mqtt_publish("cmnd/SwitchProba2/POWER2", 'ON')
        #client.converted_message = "None"
        #kuchniaSwitchStatus = "ON"

# if client.topic == "stat/SwitchProba2/POWER2" and client.converted_message == "ON":
#     client.mqtt_publish("cmnd/SwitchProba2/POWER1", 'ON')
#     client.converted_message = "None"
#
# if client.topic == "stat/SwitchProba2/POWER2" and client.converted_message == "OFF":
#     client.mqtt_publish("cmnd/SwitchProba2/POWER1", 'OFF')
#     client.converted_message = "None"

#  client.mqtt_subscribe("/plus")
# client.mqtt_subscribe("/minus")
# while True:
# print(client.converted_message)
# if (client.topic == "stat/SwitchProba2/POWER1" or client.topic == "stat/SwitchKuchnia/POWER1") and client.converted_message == 'ON':
#    print(f'Kuchnia ON and {client.topic}')
#    client.mqtt_publish("cmnd/SwitchKuchnia/POWER1", 'ON')
#    client.mqtt_publish("cmnd/SwitchProba2/POWER1", 'ON')
#    client.converted_message = 'None'


# if (client.topic == "stat/SwitchProba2/POWER1" or client.topic == "stat/SwitchKuchnia/POWER1") and client.converted_message == 'OFF':
#     print(f'Kuchnia OFF and {client.topic}')
#     client.mqtt_publish("cmnd/SwitchKuchnia/POWER1", 'OFF')
#     client.mqtt_publish("cmnd/SwitchProba2/POWER1", 'OFF')
#     client.converted_message = 'None'


# if (client.topic == "stat/SwitchProba2/POWER1" or client.topic == "stat/SwitchKuchnia/POWER1") and client.converted_message == 'OFF':
#    print(f'Kuchnia OFF and {client.topic}')
#    client.mqtt_publish("cmnd/SwitchProba2/POWER1", 'OFF')
#    client.mqtt_publish("cmnd/SwitchKuchnia/POWER1", 'OFF')
#    client.converted_message = 'None'

# if (client.topic == "stat/SwitchProba2/POWER1" or client.topic == "stat/SwitchKuchnia/POWER1") and client.converted_message == 'ON':
#    print(f'Kuchnia ON and {client.topic}')
#    client.mqtt_publish("cmnd/SwitchProba2/POWER1", 'ON')
#    client.mqtt_publish("cmnd/SwitchKuchnia/POWER1", 'ON')
#    client.converted_message = 'None'
#         controller.write_memory(2, 0, 1, client.converted_message)
#         controller.write_memory(2, 1, 1, client.converted_message)
