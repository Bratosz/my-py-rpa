employee_number = 0
plant_number = 1
department = 2
first_name = 3
last_name = 4
locker = 5
box = 6
article_number = 7
size = 9
modification = 10
badge = 11
quantity = 12

plant_number_for_dismiss = 6
last_name_for_dismiss = 1
locker_number_for_dismiss = 4
box_number_for_dismiss = 5


def get_plant_number(row):
    return int_value_of(row[plant_number].value)


def get_plant_number_for_dismiss(row):
    return int_value_of(row[plant_number_for_dismiss].value)


def get_department(row):
    value = string_value_of(row[department].value)
    if value == 'None':
        return ' '
    else:
        return value


def get_employee_number(row):
    return int_value_of(row[employee_number].value)


def int_value_of(value):
    if type(value) == 'int':
        return value
    else:
        return int(value)


def string_value_of(value):
    if type(value) == 'str':
        return value
    elif value is None:
        return ''
    else:
        return str(value)


def get_employee(row):
    return Employee(string_value_of(row[employee_number].value),
                    string_value_of(row[plant_number].value),
                    get_department(row),
                    string_value_of(row[first_name].value),
                    string_value_of(row[last_name].value),
                    string_value_of(row[locker].value),
                    string_value_of(row[box].value))


def get_employee_for_dismiss(row):
    return Employee_For_Dismiss(string_value_of(row[last_name_for_dismiss].value),
                                string_value_of(row[plant_number_for_dismiss].value),
                                string_value_of(row[locker_number_for_dismiss].value),
                                string_value_of(row[box_number_for_dismiss].value))


def get_article(row):
    return Article(string_value_of(row[article_number].value),
                   string_value_of(row[size].value),
                   string_value_of(row[modification].value),
                   string_value_of(row[badge].value),
                   string_value_of(row[quantity].value))


class Article:
    def __init__(self,
                 article_number,
                 size,
                 modification,
                 badge,
                 quantity):
        self.__article_number = article_number
        self.__size = size
        self.__modification = modification
        self.__badge = badge
        self.__quantity = quantity

    def get_article_number(self):
        return self.__article_number

    def get_size(self):
        return self.__size

    def get_modification(self):
        return self.__modification

    def get_badge(self):
        return self.__badge

    def get_quantity(self):
        return self.__quantity


class Employee_For_Dismiss:
    def __init__(self,
                 last_name,
                 plant_number,
                 locker_number,
                 box_number):
        self.__last_name = last_name
        self.__plant_number = plant_number
        self.__locker_number = locker_number
        self.__box_number = box_number

    def get_last_name(self):
        return self.__last_name

    def get_plant_number(self):
        return self.__plant_number

    def get_locker_number(self):
        return self.__locker_number

    def get_box_number(self):
        return self.__box_number

class Employee:
    def __init__(self,
                 employee_number,
                 plant_number,
                 department,
                 first_name,
                 last_name,
                 locker,
                 box):
        self.__employee_number = employee_number
        self.__plant_number = plant_number
        self.__department = department
        self.__first_name = first_name
        self.__last_name = last_name
        self.__locker = locker
        self.__box = box

    def get_employee_number(self):
        return self.__employee_number

    def get_plant_number(self):
        return self.__plant_number

    def get_department(self):
        return self.__department

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_locker(self):
        return self.__locker

    def get_box(self):
        return self.__box
