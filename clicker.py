import pynput.mouse as ms
import pynput.keyboard as kb
from pynput.mouse import Listener, Button
from pynput.keyboard import Key
from time import sleep

mouse = ms.Controller()
keyboard = kb.Controller()

NL = (1306, 263) #Next Level
LU = (485, 448)  #Level Up
bg = (1245, 596) #bad guy
noc = 0 #Number of clicks

mouse.position = bg


def levelup():
    mouse.position = LU
    keyboard.press(Key.ctrl)
    mouse.click(Button.left)
    keyboard.release(Key.ctrl)


def nextlevel():
    mouse.position = NL
    mouse.click(Button.left)


def coincollctor():
    mouse.move(0, 25)
    sleep(0.01)
    mouse.move(100, 0)
    sleep(0.01)
    mouse.move(-200, 0)
    sleep(0.01)
    mouse.position = bg
    sleep(0.01)


while mouse.position == bg or mouse.position == LU or mouse.position == NL:
    noc = noc + 1

    sleep(0.01)
    mouse.click(Button.left)

    coincollctor()

    if noc == 20:
        levelup()
        nextlevel()

        mouse.position = bg

        noc = 0


def poiner():
    if mouse.position != bg:
        return False


with Listener(on_move=poiner) as listener:
    listener.join()
