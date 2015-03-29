#! /usr/bin/python
import serial
import time
#from serial import serial

# open serial port
try:
	port = "/dev/rfcomm0"
	baudrate = 115200
	ser=serial.Serial(port,baudrate)
except serial.SerialException as e:
	print("could not open serial port '{}':{}".format(port,e))

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
while 1:
#recieve
	time.sleep(1)
	if ser.inWaiting() > 0:
#		print(ser.inWaiting())
		print ser.read(ser.inWaiting())
#		for i in range(ser.inWaiting()):
#			print(i,bytes([i]))
#			print(i,ser.read(1))
#		print(ser.readline())
#	for c in ser.read():
#		seq.append(chr(c)) #convert from ANSII
#		joined_seq = ''.join(str(v) for v in seq) #Make a string from array
##		if chr(c) == '\n':
#			print("Line " + str(count) + ': ' + joined_seq)		
#			seq = []
##			count += 1
#			break
#		print(str(count) + str(':') + chr(line))
#		count = count+1
#	line = ser.readline()
#	print(lines.append(line.decode('utf-8').rstrip()))
	

	#wait for new data after each line
#	timeout = time.time() + 0.1
#	while not ser.inWaiting() and timeout > time.time():
#		pass
#	if not ser.inWaiting():
#		break
ser.close()
