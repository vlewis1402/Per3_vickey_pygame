from gpiozero import Button
button = Button(2)
button2 = Button(3)
button.wait_for_press()
button2.wait_for_press()
print("Never gonna give you up never gonna let you down never gonna run around and desert you never gonna make you cry never gonna say goodbye never gonna tell a lie and hurt you")
