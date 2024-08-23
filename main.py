from gpiozero import LED
from time import sleep

led = LED(17)
blink_count = int(input("Enter the number of times the LED should blink:"))

while blink_count > 0:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    blink_count -=1
print("Blinking completed!")