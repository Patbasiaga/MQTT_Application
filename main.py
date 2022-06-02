from mqtt import MQTT
import time
from random import uniform
from hub_comm import PLC

kuchniaSwitchStatus = "OFF"
client = MQTT()
# controller = PLC()
# controller.connect()
client.connect_mqtt()

while True:  # controller.check_state():
    if (
            client.topic == "stat/SwitchKuchnia/POWER1" or "stat/SwitchProba2/POWER2") and client.converted_message == "OFF" and kuchniaSwitchStatus == "ON":
        client.mqtt_publish("cmnd/SwitchKuchnia/POWER1", 'OFF')
        client.mqtt_publish("cmnd/SwitchProba2/POWER2", 'OFF')
        client.converted_message = "None"
        kuchniaSwitchStatus = "OFF"

    if (
            client.topic == "stat/SwitchKuchnia/POWER1" or "stat/SwitchProba2/POWER2") and client.converted_message == "ON" and kuchniaSwitchStatus == "OFF":
        client.mqtt_publish("cmnd/SwitchKuchnia/POWER1", 'ON')
        client.mqtt_publish("cmnd/SwitchProba2/POWER2", 'ON')
        client.converted_message = "None"
        kuchniaSwitchStatus = "ON"

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
