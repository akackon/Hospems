from gpiozero import Button, Buzzer
from postJsonWithFlask import PostWithJson

global button
global buzzer
button = Button(2)
buzzer = Buzzer(17)

def pressButton():
    buzzer.on()
    PostWithJson()
    buzzer.off()
    return "Posted Successfully"

while True:
    button.when_pressed = pressButton