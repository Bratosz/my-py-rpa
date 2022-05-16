import pyautogui

from files.managers import area_manager
from files.managers.data_writer import write_to_with_alert_check, write_size_to, copy_to


def click_plants():
    area_manager.click_plants()


def click_and_paste_plant_number(plant_number):
    area_manager.Area(area_manager.plants_plant_number).copy_to(plant_number)


class GuiDismissEmployeesManager:

    def __init__(self):
        self.__areas = area_manager.AllEmployeesAreas()
        self.__buttons = area_manager.AllEmployeesButtons()

    def click_return_button(self):
        self.__buttons.click_return_button()

    def click_all_employees_button(self):
        self.__buttons.click_all_employees_button()

    def load_all_employees_areas(self):
        self.__areas.load_areas()

    def go_to_employee(self, employee):
        copy_to(self.__areas.last_name_area, employee.get_last_name())
        copy_to(self.__areas.locker_number_area, employee.get_locker())
        copy_to(self.__areas.box_number_area, employee.get_box())
        pyautogui.press('enter')
        self.__buttons.click_clothes_button()

