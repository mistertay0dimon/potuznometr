from colorama import Fore, init
import os
import time
init()

print("Вимірюємо потужність...")
time.sleep(3)
os.system('title УВАГА! КРИТИЧНИЙ РІВЕНЬ ПОТУЖНОСТИ')
while True:
    print(Fore.RED + "УВАГА! КРИТИЧНИЙ РІВЕНЬ ПОТУЖНОСТИ")
