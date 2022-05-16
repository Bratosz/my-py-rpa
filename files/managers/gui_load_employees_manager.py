import time
from files.managers import area_manager
from files.managers.data_writer import write_to_with_alert_check, write_size_to, copy_to, copy_last_name_to, write_modification_to, \
    write_badge_to, write_to


def click_local_work():
    area_manager.click_local_work()


class Gui_Load_Employees_Manager:
    __first_name = ""
    __last_name = ""
    __locker_number = ""
    __box_number = ""
    __article_number = ""
    __size = ""
    __modification = ""
    __badge = ""
    __quantity = ""

    def __init__(self):
        self.__areas = area_manager.Local_Work_Areas()
        self.__buttons = area_manager.LocalWorkButtons()


    def __changed(self, a, b):
        if a == b:
            return False
        else:
            return True

    def put_article(self, article):
        if self.__changed(self.__article_number, article.get_article_number()):
            write_to(self.__areas.article_number, article.get_article_number())
        if self.__changed(self.__size, article.get_size()):
            write_size_to(self.__areas.size, article.get_size())
        if self.__changed(self.__modification, article.get_modification()):
            write_modification_to(self.__areas.modification, article.get_modification())
        if self.__changed(self.__badge, article.get_badge()):
            write_badge_to(self.__areas.badge, article.get_badge())
        if self.__changed(self.__quantity, article.get_quantity()):
            write_to(self.__areas.quantity, article.get_quantity())
        self.__set_actual_article(article)

    def __reset_values(self):
        self.__first_name = ""
        self.__last_name = ""
        self.__locker_number = ""
        self.__box_number = ""
        self.__article_number = ""
        self.__size = ""
        self.__modification = ""
        self.__badge = ""
        self.__quantity = ""

    def __set_actual_article(self, article):
        self.__article_number = article.get_article_number()
        self.__size = article.get_size()
        self.__modification = article.get_modification()
        self.__badge = article.get_badge()
        self.__quantity = article.get_quantity()

    def __set_actual_employee(self, employee):
        self.__first_name = employee.get_first_name()
        self.__last_name = employee.get_last_name()
        self.__locker_number = employee.get_locker()
        self.__box_number = employee.get_box()

    def save_data(self):
        self.__reset_values()
        self.__buttons.save_data.click_it()
        self.__buttons.click_do_not_print_labels()
        self.__buttons.click_close_print_view()

    def go_back_to_local_work(self):
        self.__buttons.click_local_work()
        time.sleep(1)

    def put_plant_and_department(self, employee):
        write_to_with_alert_check(self.__areas.plant_number, employee.get_plant_number())
        time.sleep(0.5)
        copy_to(self.__areas.department_name, employee.get_department())

    def put_employee(self, employee):
        if self.__changed(self.__first_name, employee.get_first_name()):
            copy_to(self.__areas.first_name, employee.get_first_name())
        if self.__changed(self.__last_name, employee.get_last_name()):
            copy_last_name_to(self.__areas.last_name, employee.get_last_name())
        if self.__changed(self.__locker_number, employee.get_locker()):
            write_to_with_alert_check(self.__areas.locker_number, employee.get_locker())
        if self.__changed(self.__box_number, employee.get_box()):
            write_to_with_alert_check(self.__areas.box_number, employee.get_box())
        self.__set_actual_employee(employee)

    def submit(self):
        self.__buttons.add_record.click_it()
        time.sleep(0.5)
