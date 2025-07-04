import serial
import json
import time
import paho.mqtt.client as mqtt

serial_port = "/dev/ttyACM0"
baud_rate = 115200
mqtt_broker = "core-mosquitto"
mqtt_port = 1883
mqtt_username = "mqttclient"
mqtt_password = "growcontrol123"
mqtt_topic = "growcontrol/ssr_status"

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_password)
client.connect(mqtt_broker, mqtt_port, 60)

ser = serial.Serial(serial_port, baud_rate, timeout=1)

while True:
    try:
        line = ser.readline().decode("utf-8").strip()
        if line.startswith("{") and line.endswith("}"):
            print("Sende an MQTT:", line)
            client.publish(mqtt_topic, line)
        time.sleep(0.1)
    except Exception as e:
        print("Fehler:", e)
        time.sleep(1)
