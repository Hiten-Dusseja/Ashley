import pywhatkit
import time
import pyautogui
import keyboard as k
from datetime import datetime


def sendmesage(phnnumber, message_sent):
    now = datetime.now()

    current_time = now.strftime("%H:%M")
    hour = int(current_time[:2])
    minu = int(current_time[3:5])
    print("Current Time =", hour, " ", minu)
    if(minu == 59 or minu == 60):
        minu = 0
        hour = hour + 1
    else:
        minu = minu+1
    pywhatkit.sendwhatmsg(phnnumber, message_sent, hour, minu)
    pyautogui.click(1090, 950)
    time.sleep(2)
    k.press_and_release('enter')


sendmesage("+919881010419", "Hello There buddy")
