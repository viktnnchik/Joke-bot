import time, pyautogui, keyboard

time.sleep(5)
f = open('viktor.txt', 'r')
for line in f:
    time.sleep(1)
    if not keyboard.is_pressed('space'):
        pyautogui.typewrite(line)
        time.sleep(1.5)
        pyautogui.press('enter')
    else:
        break



