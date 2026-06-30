import board
import busio
from PIL import Image, ImageDraw
import adafruit_ssd1306

# OLED config
WIDTH = 128
HEIGHT = 64

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# Clear display
oled.fill(0)
oled.show()

# Create image buffer
image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

# Draw text
draw.text((0, 0), "OLED WORKING!", fill=255)
draw.text((0, 20), "Raspberry Pi 4B+", fill=255)
draw.text((0, 40), "Addr: 0x3C", fill=255)

# Display
oled.image(image)
oled.show()
