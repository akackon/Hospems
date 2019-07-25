from gpiozero import Button, Buzzer
from postJsonWithFlask import PostWithJson
import time

global button
global buzzer
button = Button(2)
buzzer = Buzzer(17)

def pressButton():
    buzzer.on()
    PostWithJson()
    time.sleep(5)
    buzzer.off()
    print ("Posted Successfully")

while True:
    button.when_pressed = pressButton