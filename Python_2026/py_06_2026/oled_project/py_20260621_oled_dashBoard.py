import time
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import psutil
import socket
import os

# OLED setup
WIDTH = 128
HEIGHT = 64

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

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

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    ip = get_ip()

    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)

    draw.text((0, 0), f"CPU: {cpu}%", font=font, fill=255)
    draw.text((0, 12), f"RAM: {ram}%", font=font, fill=255)
    draw.text((0, 24), f"Disk: {disk}%", font=font, fill=255)
    draw.text((0, 36), f"IP: {ip}", font=font, fill=255)
    draw.text((0, 52), "OLED Dashboard", font=font, fill=255)

    oled.image(image)
    oled.show()

    time.sleep(1)
