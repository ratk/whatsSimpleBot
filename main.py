import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("./smiley_paperclip.png", confidence=.5)

x = position1[0]
y = position1[1]

# gets message
def get_message():
    global x, y

    position1 = pt.locateOnScreen("smiley_paperclip.png", confidence=.5)
    x = position1[0]
    y = position1[1]

    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 70, y - 43, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsappMessage = pyperclip.paste()
    pt.click()
    print("Mensage recebida: " + whatsappMessage)
    
    return whatsappMessage

def post_response(message):
    global x, y

    position1 = pt.locateOnScreen("smiley_paperclip.png", confidence=.5)
    x = position1[0]
    y = position1[1]

    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)
#    pt.typewrite("\n", interval=.01)


post_response(get_message())
