import serial
import sys

try:
    with serial.Serial("/dev/ttyS0") as s:
        s.baudrate = 115200
        s.bytesize = serial.EIGHTBITS
        s.parity = serial.PARITY_NONE
        s.stopbits = serial.STOPBITS_ONE
        s.timeout = None

        while True:
            nmea = s.readline()
            nmea = nmea.strip().decode()
            print(nmea)

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

print("Session regularly closed!")
