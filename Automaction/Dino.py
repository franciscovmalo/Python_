from PIL import ImageGrab
import pyautogui
from selenium import webdriver
aux = 0

#navegador = webdriver.Chrome()
#pyautogui.press('tab', 2)
#pyautogui.write('chrome://dino')
#pyautogui.press('enter')
#pyautogui.sleep(0.8)
#pyautogui.press('space', 2)
while True:
    
    
    screen = ImageGrab.grab()
    for t in range(330+int(aux), 400+int(aux)):

        area = screen.getpixel((t, 515))

        if area[0] == 83 or 87:
            pyautogui.press('up')

            break
        
    aux == 0.0001
   