from gpiozero import LED
from time import sleep


led = LED(17)


blink_count = int(input("Enter the number of times the LED should blink: "))


for _ in range(blink_count):
    led.on()  
    sleep(1)  
    led.off()  
    sleep(1)  

print("Blinking completed!")
