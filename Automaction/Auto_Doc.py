import pyautogui
import time


def Enter():
    pyautogui.press('enter')

def Page():
    pyautogui.hotkey('alt', 'n')  
    wait()
    pyautogui.hotkey('alt', 'n', 'p')

def wait():
    time.sleep(1.6)

def Auto():
    
    pyautogui.PAUSE =  1.5
    pyautogui.alert("A Digitação Vai Iniciar!")
    wait()
    pyautogui.press('win')
    pyautogui.write('word')
    pyautogui.PAUSE =  1.5
    wait()
    wait()    
    pyautogui.hotkey('alt', 'f4')
    wait()
    Enter()
    wait()
    wait()
    Enter()
    wait()   
      
    pyautogui.hotkey('ctrl', 'j')
    wait() 
    Page()
    wait()
    Page()
    wait()
    Page()
    wait()
    pyautogui.write('Introducao')
    Enter()
    wait()

    Page()
    Enter()

    wait()
    
    Page()
    wait()
    pyautogui.write('Conclusao')
    wait()

    Page()
    wait()
    pyautogui.write('Bibliografia')
    wait()
    pyautogui.hotkey('alt', 'h')
    wait()
    Enter()
    wait()
    pyautogui.hotkey('ctrl', 'a')   
    wait()
    wait()
    pyautogui.click(837, 102)
    pyautogui.hotkey('ctrl', 'home')
    pyautogui.hotkey('alt', 'g')
    pyautogui.hotkey('alt', 'p', 'b')
    
    #pyautogui.hotkey('alt', 'g')
    #pyautogui.hotkey('alt', 'p', 'b')
    pyautogui.hotkey('alt', 'x')
    pyautogui.hotkey('alt', 'l')
    pyautogui.press('down', 2)
    #pyautogui.press('down')
    pyautogui.press('enter', 2)
    pyautogui.alert('O Teu Documento Está Pronto!')

    
Auto()

