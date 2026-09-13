import paho.mqtt.client as mqtt

broker = "127.0.0.1"
port = 1883
topic = "yantraSthiti/test"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect(broker, port)

client.publish(topic, "Hello from Python")

client.disconnect()

print("MQTT message published")


