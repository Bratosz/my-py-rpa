from openpyxl import load_workbook

def get_rows(file_name):
    file_path = 'raporty/' + file_name + '.xlsx'
    book = load_workbook(file_path)
    sheet = book.worksheets[0]
    rows = sheet.rows
    headers = [cell.value for cell in next(rows)]
    return rows
