import spidev as SPI
import ST7789
import time
import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
IS_ALL_GROUPS = False

from PIL import Image,ImageDraw,ImageFont

# Define the display
W = 240
H = 240

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 24
bus = 0
device = 0

# 240x240 display with hardware SPI:
disp = ST7789.ST7789(SPI.SpiDev(bus, device),RST, DC, BL)

# Configure fonts used
font1 = ImageFont.truetype("Gidole-Regular.ttf", size=36)
font2 = ImageFont.truetype("Gidole-Regular.ttf", size=24)

# Find the IP address and hostname of this host
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("192.168.16.1", 80))
message2 = s.getsockname()[0]
s.close()
message3 = socket.gethostname()

# Initialize display library
disp.Init()

# Clear display.
disp.clear()

# Create blank image for drawing.
backdrop = Image.new("RGB", (disp.width, disp.height), "BLACK")
draw = ImageDraw.Draw(backdrop)

# Put a red background at the top of the screen
draw.rectangle([(10,10),(240,120)],fill = "RED")

# Set a default message
message1 = 'No Data'

# Find the centre of the message
w, h = draw.textsize(message1, font=font1)
draw.text(((W-w)/2, 50), message1, fill = "BLACK", font=font1)

w, h = draw.textsize(message2, font=font2)
draw.text(((W-w)/2, 160), message2, fill = "WHITE", font=font2)

w, h = draw.textsize(message3, font=font2)
draw.text(((W-w)/2, 200), message3, fill = "WHITE", font=font2)

disp.ShowImage(backdrop,0,0)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if IS_ALL_GROUPS:
  # on this port, receives ALL multicast groups
  sock.bind(('', MCAST_PORT))
else:
  # on this port, listen ONLY to MCAST_GRP
  sock.bind((MCAST_GRP, MCAST_PORT))

# Set multicast options  
mreq = struct.pack('4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:

  data = (sock.recv(10240))
  payload = data.decode('utf-8')
  list_of_values = payload.split(',')
  talker_id = list_of_values[0][0:-3]
  sentence_id = list_of_values[0][3:]

  if sentence_id == 'HDT':
    # Provide some feedback on the screen
    print(payload)
    # Get the heading value, do not worry about CRC, this is a display only
    heading_float = float(list_of_values[1])
    # Round to 2 decimal places and add bling
    heading_round = "%.2f" % heading_float
    message1 = str(heading_round) + ' ºT'
    # Now update the screen
    draw.rectangle([(10,10),(240,120)],fill = "GREEN")
    w, h = draw.textsize(message1, font=font1)
    draw.text(((W-w)/2, 50), message1, fill = "WHITE", font=font1)
    disp.ShowImage(backdrop,0,0)



