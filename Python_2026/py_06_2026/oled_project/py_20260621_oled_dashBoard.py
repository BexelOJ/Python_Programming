import json
import paho.mqtt.client as mqtt
import time
import psycopg
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import psutil
import socket
import os

# MQTT setup
MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "yantraSthiti/metrics"

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
    print("MQTT connected")
except Exception as e:
    print(f"MQTT connection failed: {e}")
    mqtt_client = None

# OLED setup
WIDTH = 128
HEIGHT = 64

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

def connect_database():
    try:
        conn = psycopg.connect(
            host="127.0.0.1",
            port=5432,
            dbname="yantraSthiti_DB",
            user="monitor_yantrasthiti_app",
            password="SUPPORt@1615"
        )

        print("PostgreSQL connected")
        return conn

    except Exception as e:
        print(f"PostgreSQL connection failed: {e}")
        return None

# PostgreSQL setup
db_conn = connect_database()

# Clear display
oled.fill(0)
oled.show()

# Image buffer
image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

# Font (default)
font = ImageFont.load_default()

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "No WiFi"

def save_to_database(conn, ip, cpu, ram, disk):

    if conn is None:
        return None

    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO system_metrics
                (timestamp, device_id, ip, cpu, ram, disk)
                VALUES (NOW(), %s, %s, %s, %s, %s)
                """,
                (
                    "Ei Labs Server_01",
                    ip,
                    cpu,
                    ram,
                    disk
                )
            )

        conn.commit()

        return conn

    except Exception as e:
        print(f"PostgreSQL insert failed: {e}")

        try:
            conn.rollback()
        except Exception:
            pass

        return None

def publish_mqtt(client, timestamp, device_id, ip, cpu, ram, disk):

    if client is None:
        return

    try:
        data = {
            "timestamp": timestamp,
            "device_id": device_id,
            "ip": ip,
            "cpu": cpu,
            "ram": ram,
            "disk": disk
        }

        payload = json.dumps(data)

        client.publish(
            MQTT_TOPIC,
            payload
        )

    except Exception as e:
        print(f"MQTT publish failed: {e}")

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    ip = get_ip()

    timestamp = time.strftime(
        "%Y-%m-%dT%H:%M:%S%z"
    )

    device_id = "Ei Labs Server_01"

    db_conn = save_to_database(
    	db_conn,
     	ip,
    	cpu,
    	ram,
    	disk
    )    

    publish_mqtt(
        mqtt_client,
        timestamp,
        device_id,
        ip,
        cpu,
        ram,
        disk
    )

    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)

    draw.text((0, 0), f"CPU:    {cpu}%", font=font, fill=255)
    draw.text((0, 12), f"RAM:    {ram}%", font=font, fill=255)
    draw.text((0, 24), f"Disk:    {disk}%", font=font, fill=255)
    draw.text((0, 36), f"IP: {ip}", font=font, fill=255)
    draw.text((0, 52), "Ei Labs Server_01", font=font, fill=255)

    oled.image(image)
    oled.show()

    time.sleep(1)
