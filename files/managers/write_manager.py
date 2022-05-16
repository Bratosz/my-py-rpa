import pyautogui

import files.managers.gui_load_employees_manager
import time

from files.managers import row_reader, excel_reader

gui_load_employees = files.managers.gui_load_employees_manager
gui_dismiss_employees = files.managers.guidismissemployeesmanager


def __its_department_changed(previous, actual):
    if previous == '':
        return False
    elif actual == previous:
        return False
    else:
        return True


def __its_plant_changed(previous, actual):
    previous = int(previous)
    if previous == 0:
        return False
    elif previous == actual:
        return False
    else:
        return True


def __its_employee_changed(previous, actual):
    previous = int(previous)
    if previous == 0:
        return True
    elif previous == actual:
        return False
    else:
        return True


def dismiss_employees(file_name):
    plant_number = 0
    print('--start--')
    rows = excel_reader.get_rows(file_name)
    print('--wczytano plik excel--')
    print('--rozpoczęto zawalnianie pracowników--')

    gui_dismiss_employees.click_plants()
    time.sleep(1)

    gui = gui_dismiss_employees.GuiDismissEmployeesManager()

    for row in rows:
        employee = row_reader.get_employee_for_dismiss(row)
        if plant_number == 0:
            plant_number = employee.get_plant_number()
            gui_dismiss_employees.click_and_paste_plant_number(plant_number)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            gui.click_all_employees_button()
            time.sleep(0.5)
            gui.load_all_employees_areas()
        elif __its_plant_changed(plant_number, employee.get_plant_number()):
            plant_number = employee.get_plant_number()
            gui_dismiss_employees.click_and_paste_plant_number(plant_number)
            gui.click_all_employees_button()
            time.sleep(0.5)
            gui.load_all_employees_areas()
            gui.go_to_employee(employee)





def load_employees(file_name):
    print('--start--')
    employee_number = 0
    plant_number = 0
    department_name = ''
    rows = excel_reader.get_rows(file_name)
    time.sleep(0.5)
    print('--wczytano plik excel--')
    time.sleep(0.5)
    print('--rozpoczęto przypisywanie pracowników--')

    gui_load_employees.click_local_work()
    time.sleep(1)
    gui = gui_load_employees.Gui_Load_Employees_Manager()

    for row in rows:
        if __its_employee_changed(employee_number, row_reader.get_employee_number(row)):
            if __its_plant_changed(plant_number, row_reader.get_plant_number(row)):
                gui.save_data()
                gui.go_back_to_local_work()
                gui.put_plant_and_department(row_reader.get_employee(row))
            elif __its_department_changed(department_name, row_reader.get_department(row)):
                gui.save_data()
                gui.go_back_to_local_work()
                gui.put_plant_and_department(row_reader.get_employee(row))
            if employee_number == 0:
                gui.put_plant_and_department(row_reader.get_employee(row))
            gui.put_employee(row_reader.get_employee(row))
            gui.put_article(row_reader.get_article(row))
            gui.submit()
            employee_number = row_reader.get_employee_number(row)
            plant_number = row_reader.get_plant_number(row)
            department_name = row_reader.get_department(row)
        else:
            gui.put_article(row_reader.get_article(row))
            gui.submit()
    print('--zakończono przypisywanie pracownikow--')
