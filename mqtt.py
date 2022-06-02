import paho.mqtt.client as mqtt

MQTT_SERVER_ADDRESS = 'mqtt.flespi.io'
USERNAME = "el30F7IQyOctoTGHNAYGv8YO9eYkvCezO5oh3UXryXILFciiA6OV3Dy0Fka0Meoo"
PASSWORD = ""
TOPICS = ['stat/SwitchKuchnia/POWER1', 'stat/SwitchProba2/POWER1', 'stat/SwitchProba2/POWER2', 'cmnd/SwitchProbe2/POWER2' , 'cmnd/SwitchTest/POWER1']


class MQTT:
    def __init__(self):
        self.mqtt_client = mqtt.Client()
        self.converted_message = 0
        self.topic = ''

    def on_connect(self, client, userdata, flags, rc):
        for topic in TOPICS:
            self.mqtt_subscribe(topic)
        print("Connected with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        print(f"Received '{msg.payload.decode('utf-8')}' from '{msg.topic}' topic")
        self.topic = msg.topic
        msg.topic = ''

       # try:
        self.converted_message = msg.payload.decode('utf-8')
      #  except:
       #     print("Recived Data Is Not Integer Number")

    def connect_mqtt(self):
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        try:
            print("connecting to mqtt server " + str(MQTT_SERVER_ADDRESS))
            self.mqtt_client.username_pw_set(USERNAME, PASSWORD)
            self.mqtt_client.connect(MQTT_SERVER_ADDRESS, 1883, 60)
            self.mqtt_client.loop_start()

        except Exception as e:
            print("Unable to connect to MQTT server" + str(MQTT_SERVER_ADDRESS))

    def disconnect_mqtt(self):
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()

    def mqtt_publish(self, topic, msg):
        self.mqtt_client.publish(topic, msg)
        print(f'Successful published {msg} to {topic}')

    def mqtt_subscribe(self, topic):
        self.mqtt_client.subscribe(topic)

