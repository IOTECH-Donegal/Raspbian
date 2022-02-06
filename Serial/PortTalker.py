import serial
import sys
from datetime import datetime
import time

comport = 'COM16'

try:
    with serial.Serial(comport) as s:
        s.baudrate = 115200
        s.bytesize = serial.EIGHTBITS
        s.parity = serial.PARITY_NONE
        s.stopbits = serial.STOPBITS_ONE
        s.timeout = None

        while True:
            now = datetime.now()
            this_time = now.strftime("%H:%M:%S")
            this_time_bytes = bytes(this_time, 'utf-8')
            s.write(this_time_bytes)
            print(f'Sent {this_time} to port {comport}')
            time.sleep(2)

except serial.SerialException as err:
    print("Serial Port Error: \n" + str(err))
    sys.exit()
except KeyboardInterrupt:
    print("Keyboard break")
    sys.exit()
except Exception as err:
    print("An error has occurred!")
    print(err)
    sys.exit()



