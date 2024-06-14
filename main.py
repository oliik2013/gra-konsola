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
y = 1
d1 = "############################"
d2 = "#                          #" # Tutaj y = 6
d3 = "#                          #"
d4 = "#                          #" 
d5 = "#                          #"
d6 = "#                          #"
d7 = "#            v             #" # Tutaj y = 1
d8 = "############################" 
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
        if y == 1 or 2 or 3 or 4 or 5:
            y += 1
        if y == 2 and x == 14:
            d7 = "#                          #"
            d6 = "#            v             #"
        if y == 3 and x == 14:
            d6 = "#                          #"
            d5 = "#            v             #" 
        if y == 4 and x == 14:
            d5 = "#                          #"
            d4 = "#            v             #"
        if y == 5 and x == 14:
            d4 = "#                          #"
            d3 = "#            v             #"
        if y == 6 and x == 14:
            d3 = "#                          #"
            d2 = "#            v             #"
        if y == 7:
            y = 6

    if keyboard.read_key() == "s":
        if y == 1:
            y = 2
        if y == 2 and x == 14:
            d6 = "#                          #"
            d7 = "#            v             #"
        if y == 3 and x == 14:
            d5 = "#                          #"
            d6 = "#            v             #"
        if y == 4 and x == 14:
            d4 = "#                          #"
            d5 = "#            v             #"
        if y == 5 and x == 14:
            d3 = "#                          #"
            d4 = "#            v             #"
        if y == 6 and x == 14:
            d2 = "#                          #"
            d3 = "#            v             #"
        if y == 2 or 3 or 4 or 5 or 6:
            y -= 1

    clear()

    