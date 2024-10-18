# Auteur : Matteo Lemee  ;  Date de création : 18/10/2024

import time
from plyer import notification
import winsound
import platform

def notif():
    heure = time.localtime()
    message = f"Il est actuellement {heure.tm_hour}:{heure.tm_min}"
    notification.notify(title="Rappel Heure", message = message, timeout=15)

def alerte():
    système = platform.system()
    if système == "Windows":
        winsound.Beep(1200,1500) #(fréquence,durée seconde)
    else : 
        print("L'os n'est pas pris en charge")

while True:
    heure = time.localtime()
    minute = heure.tm_min

    if minute == 0:
        notif()
        alerte()
        time.sleep(60)
    
    time.sleep(1)
