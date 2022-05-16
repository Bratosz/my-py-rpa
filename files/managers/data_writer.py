from files.managers.area_manager import alert_is_present_then_click_ok
import time, pyautogui

alert_wrong_data = 'files/img/alert_wrong_data.png'
button_ok_wrong_data = 'files/img/button_ok_wrong_data.png'

alert_duplicate_employee = 'files/img/alert_duplicate_employee.png'
button_ok_duplicate_employee = 'files/img/button_ok_duplicate_employee.png'

alert_duplicate_employee_pending_for_save = 'files/img/alert_duplicate_employee_pending_for_save.png'
button_ok_duplicate_employee_pending_for_save = 'files/img/button_ok_duplicate_employee_pending_for_save.png'

alert_employee_is_on_dismissal_list = 'files/img/alert_employee_is_on_dismissal_list.png'
button_ok_employee_is_on_dismissal_list = 'files/img/button_ok_employee_is_on_dismissal_list.png'


def convert_size_to_letter_notation(cloth_size):
    number = int(cloth_size[0:1])
    i = 0
    result = ''
    while i < number:
        result += 'X'
        i += 1
    return result + cloth_size[2:3]


def write_to(area, value):
    area.write_to(value)
    return True


def write_to_with_alert_check(area, value):
    area.write_to_with_alert_check(value)
    if alert_is_present_then_click_ok(alert_wrong_data, button_ok_wrong_data):
        return False
    else:
        return True


def write_modification_to(area, value):
    if value == 'None':
        area.write_to('')
    else:
        area.write_to(value)


def write_badge_to(area, value):
    if value == '0':
        area.write_to('')
    else:
        area.write_to(value)


def copy_to(area, value):
    area.copy_to(value)


def copy_last_name_to(area, value):
    area.copy_to(value)
    time.sleep(0.5)
    if alert_is_present_then_click_ok(alert_duplicate_employee,
                                      button_ok_duplicate_employee):
        double_click()
    elif alert_is_present_then_click_ok(alert_duplicate_employee_pending_for_save,
                                        button_ok_duplicate_employee_pending_for_save):
        double_click()
    elif alert_is_present_then_click_ok(alert_employee_is_on_dismissal_list,
                                        button_ok_employee_is_on_dismissal_list):
        double_click()


def double_click():
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()


def write_size_to(size_area, value):
    size_area.write_to_with_alert_check(value)
    time.sleep(0.5)
    if alert_is_present_then_click_ok(alert_wrong_data, button_ok_wrong_data):
        value = convert_size_to_letter_notation(value)
        size_area.write_to_with_alert_check(value)
        if alert_is_present_then_click_ok(alert_wrong_data, button_ok_wrong_data):
            return False
        else:
            return True
    return True
