import paho.mqtt.client as mqtt
from config import MQTT_CONFIG


class MQTT:

    def __init__(self):
        self.mqtt_client = mqtt.Client()
        self.converted_message = 0
        self.topic = ''
        self.is_connected = False
        self.received = False
        self.live_bit = 0

    def on_connect(self, client, userdata, flags, rc):
        for topic in MQTT_CONFIG.TOPICS:
            self.mqtt_subscribe(topic)
        print("Connected with result code " + str(rc))

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected")
        self.disconnect_mqtt()
        self.is_connected = False

    def on_message(self, client, userdata, msg):
        print(f"Received '{msg.payload.decode('utf-8')}' from '{msg.topic}' topic")
        self.topic = msg.topic
        self.received = True


       # try:
        self.converted_message = msg.payload.decode('utf-8')
      #  except:
       #     print("Recived Data Is Not Integer Number")

    def connect_mqtt(self):
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.on_message = self.on_message
        try:
            print("connecting to mqtt server " + str(MQTT_CONFIG.MQTT_SERVER_ADDRESS))
            self.mqtt_client.username_pw_set(MQTT_CONFIG.USERNAME, MQTT_CONFIG.PASSWORD)
            self.mqtt_client.connect(MQTT_CONFIG.MQTT_SERVER_ADDRESS, 1883, 5)
            self.mqtt_client.loop_start()
            self.is_connected = True

        except Exception as e:
            print("Unable to connect to MQTT server" + str(MQTT_CONFIG.MQTT_SERVER_ADDRESS))

    def disconnect_mqtt(self):
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()

    def mqtt_publish(self, topic, msg):
        self.mqtt_client.publish(topic, msg)
        print(f'Successful published {msg} to {topic}')

    def mqtt_subscribe(self, topic):
        self.mqtt_client.subscribe(topic)
        print(topic)

