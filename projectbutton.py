from gpiozero import Button
button = Button(2)
button2 = Button(3)
button.wait_for_press()
button2.wait_for_press()
print("Never gonna give you up ")

#What I need to do:
#- code it so that buttons give a true/false input depending on if they're being pushed
#- then they have to return whatever direction they're being pushed in
#- then we have to code Nik's game to recognize that and move with it

