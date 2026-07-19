import pyautogui
import time
import webbrowser

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.3

def open_game():
	webbrowser.open("https://neal.fun/not-a-robot")
	time.sleep(2)
	pyautogui.moveTo(36,1042)
	pyautogui.click()
	pyautogui.moveTo(1030,568)
	pyautogui.click()

def level1():
	pyautogui.moveTo(783,237)
	pyautogui.click()
	time.sleep(3)

def level2():
	pyautogui.moveTo(1033,329)
	pyautogui.click()
	pyautogui.moveTo(1173,321)
	pyautogui.click()
	pyautogui.moveTo(1032,485)
	pyautogui.click()
	pyautogui.moveTo(1173,476)
	pyautogui.click()
	pyautogui.moveTo(1186,894)
	pyautogui.click()
	time.sleep(3)


def level4():
	pyautogui.moveTo(965,266)
	pyautogui.click()
	pyautogui.moveTo(1148,283)
	pyautogui.click()
	pyautogui.moveTo(1143,471)
	pyautogui.click()
	pyautogui.moveTo(1143,681)
	pyautogui.click()
	pyautogui.moveTo(1179,895)
	pyautogui.click()

open_game()
level1()
level2()
level4()
