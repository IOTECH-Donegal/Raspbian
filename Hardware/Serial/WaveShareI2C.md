## Waveshare 

Product page can be found at https://www.waveshare.com/serial-expansion-hat.htm
Follow the instruction there to enable.
Note that at 115200 b/s the serial port is running faster than the I2C bus, loads of errors.
You need to increase the I2C bus speed.

Edit the config file 
  sudo nano /boot/config.txt


Find the line dtparam=i2c_arm=on and edit it so it reads
  
  dtparam=i2c_arm=on,i2c_arm_baudrate=400000

Note that even at the new bus speed, I cannot reliably get 115200 from both serial interfaces simultaneously.  
