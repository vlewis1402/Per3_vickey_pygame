from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(2)

while True:
    button.wait_for_press()
    led.on()
    led.toggle()
    sleep(0.5)

    button.when_pressed = led.on
    button.when_released = led.off

pause()

