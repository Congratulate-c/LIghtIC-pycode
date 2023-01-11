import pyautogui
from time import sleep





print("------------------------------->>>>>>>>>>开始操作！")
pyautogui.moveTo(1, 1, duration=0.25)
pyautogui.leftClick()
sleep(1)
c = 3
i = 1
while i<c:
    pyautogui.click(x=100, y=200,button='left')
    sleep(1)
    pyautogui.click(x=100, y=100, button='left')
    sleep(1)
    pyautogui.click(x=100, y=200, button='left')
    sleep(1)
    pyautogui.click(x=100, y=200, button='left')
    sleep(1)
    pyautogui.moveTo(100, 200, duration=0.25)
    pyautogui.doubleClick()
    sleep(0.3)
    pyautogui.click()
    sleep(1)
    pyautogui.write('fm1_100m_'+'str(n)', interval=0.25)
    sleep(1)
    i+=1

