import keyboard
import os
from time import sleep
import pyautogui
import pynput
import logging
from pynput.keyboard import Key, Listener
fps = 0.1
clear = lambda: os.system('cls')
clear()
print("Witaj w grze tylko na konsole (nie dotyczy ostrzeżenia)")
pyautogui.alert(text='Jeśli twój komputer nie wytrzymuje tej gry to zmień w skrzypcie zmienną fps na wyszą.', title='Info', button='Ok')
sleep(1)
clear()
x = 14
y = 0
d1 = "############################"
d2 = "#                          #"
d3 = "#                          #"
d4 = "#                          #" 
d5 = "#                          #"
d6 = "#                          #"
d7 = "#                          #"
d8 = "#############v##############" # Tutaj y = 0
    #Tutaj x = 14 /\

while True:
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    print(d5)
    print(d6)
    print(d7)
    print(d8)

    sleep(fps)
    
    if keyboard.read_key() == "w":
        y += 1
        print(y)

    clear()