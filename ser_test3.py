#! /usr/bin/python
import serial
import time
import RPi.GPIO as GPIO
import os.path

# BOARDpin No
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

	
# open serial port
'''
try:
	port = "/dev/rfcomm0"
	baudrate = 115200
	print(os.path.exists(port))
	ser=serial.Serial(port,baudrate)
except serial.SerialException as e:
	print("could not open serial port '{}':{}".format(port,e))
'''
while 1:
  port = "/dev/rfcomm0"
  baudrate = 115200

  if os.path.exists(port):
    ser=serial.Serial(port,baudrate)
    print("Connection OK")
    break 
# Clear input buffer
ser.flushInput()

# Clear output buffer
ser.flushOutput()

# write test
x = "pyserial test write/read\n"
ser.write(x)
print("write date: " + x)

# read response from serial port
seq = []
count=1
readdata=''
try:
  while 1:
#recieve
	time.sleep(1)
	if ser.inWaiting() > 0:
#		print(ser.inWaiting())
#		print ser.read(ser.inWaiting())
	  readdata = ser.read(ser.inWaiting())
	  print readdata
	  if readdata == 'f':
	     print("forward\n")
	     GPIO.output(7, GPIO.HIGH)
             GPIO.output(11, GPIO.LOW)
             time.sleep(1)
             GPIO.output(7, GPIO.LOW)
             GPIO.output(11, GPIO.LOW)
             time.sleep(1)
	  elif readdata == "b": 
	     print("back\n")
	     GPIO.output(7, GPIO.HIGH)
             GPIO.output(11, GPIO.LOW)
             time.sleep(1)
             GPIO.output(7, GPIO.LOW)
             GPIO.output(11, GPIO.LOW)
             time.sleep(1)
except KeyboardInterrupt:
  ser.close()
  GPIO.cleanup()
  print("Program exit\n")

