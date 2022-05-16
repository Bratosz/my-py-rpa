from os.path import exists


def file_exist(file_name):
    file_path = 'raporty/' + file_name + '.xlsx'
    return exists(file_path)
