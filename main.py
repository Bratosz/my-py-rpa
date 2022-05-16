from files.managers import write_manager
from files.managers.file_checker import file_exist

while True:
    option = input("Co chesz uczynić padawanie?\n"
                   "1. Wczytać pracowników\n"
                   "2. Zwolnić pracowników\n"
                   "Podaj liczbę: ")
    if option != "1" and option != "2":
        option = input("Nie ma takiej  opcji na liście, podaj prawidłową wartość i naciśnij ENTER.")
    else:
        break

file_name = input("Podaj nazwę pliku z listą pracowników (bez rozszerzenia): ")
while True:
    if file_exist(file_name):
        if option == "1":
            write_manager.load_employees(file_name)
        elif option == "2":
            write_manager.dismiss_employees(file_name)
        break
    file_name = input("Nazwa: " + file_name + " jest nieprawidłowa. Podaj inną: ")