import os
import readchar
from time import sleep
from sys import platform
fps = 0.1
if platform == "win32":
    clear = lambda: os.system('cls')
if platform == "linux" or platform == "linux2":
    clear = lambda: os.system('clear')
clear()
print("Witaj w grze tylko na konsole.")
sleep(1)
clear()
print("INFO: Jeśli twój komputer nie wytrzymuje tej gry to zmień w skrzypcie zmienną fps na wyszą.")
sleep(1)
clear()
x = 14
## Hi
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

    guzik = readchar.readkey()
    
    if guzik == "w" or "W":
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

    if guzik == "s" or "S":
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

    if guzik == "a" or "A":
        if x == 14:
            x = 13
        if x == 13 and y == 1:
            d6 = "#                          #"
            d7 = "#            v             #"
        if x == 12 and y == 2:
            d5 = "#                          #"
            d6 = "#           v              #"
        if x == 11 and y == 3:
            d4 = "#                          #"
            d5 = "#          v               #"
        if x == 10 and y == 4:
            d3 = "#                          #"
            d4 = "#         v                #"
        if x == 9 and y == 5:
            d2 = "#                          #"
            d3 = "#        v                 #"
        if x == 8 or 7 or 6 or 5 or 4:
            x -= 1


    clear()

    