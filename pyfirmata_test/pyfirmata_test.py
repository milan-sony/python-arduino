import time
from pyfirmata import Arduino

# Define the port where Arduino is connected
port = 'COM3'  # Replace with your port

# Establish a connection with the Arduino
board = Arduino(port)

# Set up the pin modes
led_pin = board.get_pin('d:10:o')

# Blink the LED
while True:
    # Turn the LED ON
    led_pin.write(1)  
    print("LED ON")
    time.sleep(1)
    # Turn the LED OFF
    led_pin.write(0)  
    print("LED OFF")
    time.sleep(1)