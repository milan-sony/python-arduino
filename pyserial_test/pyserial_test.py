# import serial for serial communication
import serial
# import time for adding delay
import time

# creating a  serial port object
arduino = serial.Serial('COM3',9600) 
# waiting for 1 second (just for the connection to get establish)
time.sleep(1)

# read the serial data and print it as line
print (arduino.readline())
print ("Press 1 to turn ON LED or Press 0 to turn OFF LED")

while True:
    # getting input from user
    var = input() 
    # if the value is 1, it will send 1 to arduino code else 0
    if (var == '1'): 
        arduino.write('1')
        print ("LED turned ON")
        time.sleep(1)
    
    if (var == '0'):
        arduino.write('0')
        print ("LED turned OFF")
        time.sleep(1)