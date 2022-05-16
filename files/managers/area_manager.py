import pyautogui, pyperclip, time
from pyautogui import \
    click, locateCenterOnScreen, hotkey, write


name_plant_number_local_work = 'files/img/plant_number_local_work.png'
name_department_name = 'files/img/department_name.png'
name_first_name = 'files/img/first_name.png'
name_last_name = 'files/img/last_name.png'
name_locker_number = 'files/img/locker_number.png'
name_box_number = 'files/img/box_number.png'
name_article_number = 'files/img/article_number.png'
name_size = 'files/img/size.png'
name_modification = 'files/img/modification.png'
name_badge = 'files/img/badge.png'
name_quantity = 'files/img/quantity.png'
area_check_for_local_work = 'files/img/comment.png'
area_check_for_plants = 'files/img/plants/nip.png'

plants_plant_number = 'files/img/plants/plant_number.png'

button_add_record = 'files/img/button_add_record.png'
button_local_work = 'files/img/button_local_work.png'
button_plants = 'files/img/button_plants.png'
button_save_data = 'files/img/button_save_data.png'
button_do_not_print_labels = 'files/img/button_do_not_print_labels.png'
button_close_print_view = 'files/img/button_close_print_view.png'

button_return_for_all_employees = 'files/img/all_employees/button_return.png'
button_all_employees = 'files/img/all_employees/all_employees.png'
button_clothes = 'files/img/all_employees/button_clothes.png'
button_dismiss_for_all_employees = 'files/img/all_employees/dismiss.png'
area_last_name_for_all_employees = 'files/img/all_employees/last_name.png'
area_locker_number_for_all_employees = 'files/img/all_employees/locker_number.png'
area_box_number_for_all_employees = 'files/img/all_employees/box_number.png'




def clear_it():
    hotkey('ctrl', 'backspace')
    hotkey('ctrl', 'delete')
    hotkey('ctrl', 'backspace')
    hotkey('ctrl', 'delete')


def get_location_of(image_location):
    location = locateCenterOnScreen(image_location,
                                    grayscale=True,
                                    confidence=.99)
    return location


def alert_is_present_then_click_ok(alert_name, ok_button):
    area = get_location_of(alert_name)
    if area is None:
        return False
    else:
        button_ok = Button(get_location_of(ok_button))
        button_ok.click_it()
        return True


def get_location_from_new_window(img_dir):
    location = None
    while location is None:
        location = get_location_of(img_dir)
    return location


def click_local_work():
    location = get_location_from_new_window(button_local_work)
    button = Button(location)
    button.click_it()


def click_plants():
    location = get_location_from_new_window(button_plants)
    button = Button(location)
    button.click_it()


class Plants_Areas_And_Buttons:
    def __init__(self):
        self.check_area = area_check_for_plants
        self.plant_number = Area(get_location_of(plants_plant_number), self.check_area)



class Local_Work_Areas:
    def __init__(self):
        self.check_area = area_check_for_local_work
        self.plant_number = Area(get_location_of(name_plant_number_local_work), self.check_area)
        self.department_name = Area(get_location_of(name_department_name), self.check_area)
        self.first_name = Area(get_location_of(name_first_name), self.check_area)
        self.last_name = Area(get_location_of(name_last_name), self.check_area)
        self.locker_number = Area(get_location_of(name_locker_number), self.check_area)
        self.box_number = Area(get_location_of(name_box_number), self.check_area)
        self.article_number = Area(get_location_of(name_article_number), self.check_area)
        self.size = Area(get_location_of(name_size), self.check_area)
        self.modification = Area(get_location_of(name_modification), self.check_area)
        self.badge = Area(get_location_of(name_badge), self.check_area)
        self.quantity = Area(get_location_of(name_quantity), self.check_area)


class AllEmployeesAreas:
    def __init__(self):
        self.last_name_area = None
        self.locker_number_area = None
        self.box_number_area = None
        self.button_clothes = None

    def load_areas(self):
        self.last_name_area = Area(get_location_of(area_last_name_for_all_employees))
        self.locker_number_area = Area(get_location_of(area_locker_number_for_all_employees))
        self.box_number_area = Area(get_location_of(area_box_number_for_all_employees))
        self.button_clothes = Area(get_location_of(button_clothes))


class AllEmployeesButtons:
    def __init__(self):
        self.__button_all_employees = None
        self.__button_clothes = None
        self.__return_button = Button(get_location_of(button_return_for_all_employees))

    def click_return_button(self):
        self.__return_button.click_it()

    def click_all_employees_button(self):
        location = get_location_from_new_window(button_all_employees)
        self.__button_all_employees = Button(location)
        self.__button_all_employees.click_it()

    def click_clothes_button(self):
        if self.__button_clothes is None:
            self.__button_clothes = Button(get_location_of(button_clothes))
        self.__button_clothes.click_it()



class LocalWorkButtons:
    def __init__(self):
        self.add_record = Button(get_location_of(button_add_record))
        self.save_data = Button(get_location_of(button_save_data))
        self.__local_work = ''
        self.__do_not_print_labels = ''
        self.__close_print_view = ''

    def click_do_not_print_labels(self):
        location = get_location_from_new_window(button_do_not_print_labels)
        self.__do_not_print_labels = Button(location)
        self.__do_not_print_labels.click_it()

    def click_close_print_view(self):
        location = get_location_from_new_window(button_close_print_view)
        self.__close_print_view = Button(location)
        self.__close_print_view.click_it()

    def click_local_work(self):
        location = get_location_from_new_window(button_local_work)
        self.__local_work = Button(location)
        self.__local_work.click_it()

class Button:
    def __init__(self, location):
        self.location = location

    def click_it(self):
        click(self.location)

class Area:
    def __init__(self, location, check_area):
        self.location = location
        self.__check_area_location = \
            locateCenterOnScreen(check_area,
                                 grayscale=True,
                                 confidence=.99)

    def click_and_clear(self):
        self.click_it()
        clear_it()

    def click_it(self):
        click(self.location)

    def write_to(self, value):
        self.click_and_clear()
        write(value)

    def write_to_with_alert_check(self, value):
        self.click_and_clear()
        write(value)
        self.click_check_area()

    def click_check_area(self):
        click(self.__check_area_location)

    def copy_to(self, value):
        self.click_and_clear()
        pyperclip.copy(value)
        pyautogui.hotkey('ctrl', 'v')
        click(self.__check_area_location)


