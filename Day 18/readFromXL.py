import xlrd

book = xlrd.open_workbook('Students.xlsx') # it creates a workbook object
sheets = book.sheets() # It list all sheets available in workbook

id_names = dict()
id_companies = dict()
for sheet in sheets:
    if sheet.name == 'names': # It return the sheet name
        for row in range(sheet.nrows):  # it return rows available in sheet
            id_names[sheet.cell_value(row, 0)] = sheet.cell_value(row, 1)
    elif sheet.name == 'companies':
        for row in range(sheet.nrows):  # it return rows available in sheet
            id_companies[sheet.cell_value(row, 0)] = sheet.cell_value(row, 1)

for id, name in id_names.items():
    print(name, id_companies[id])
