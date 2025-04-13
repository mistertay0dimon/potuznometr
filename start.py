from colorama import Fore, Style, init
import os
init()

print("Потужномітр")
print(Fore.YELLOW + "Лише для украінців" + Style.RESET_ALL)
print("Потужність: 0")
print("\n1: Виміряти потужність")
print("2: Вийти")

while True:
    command = input("ПОТУЖНІСТЬ: ")
    if command == "1":
        os.system('python potuzno.py') # Запуск вимріювання потужності
    elif command == "2":
        exit()
