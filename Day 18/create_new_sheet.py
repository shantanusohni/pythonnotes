import xlrd
import xlwt

create_book = xlwt.Workbook()
sheet1 = create_book.add_sheet('Students')

book = xlrd.open_workbook('Students.xlsx') # it creates a workbook object
sheets = book.sheets() # It list all sheets available in workbook

id_names = dict()
id_companies = dict()
for sheet in sheets:
    if sheet.name == 'names': # It return the sheet name
        for row in range(sheet.nrows):  # it return rows available in sheet
            if sheet.cell_value(row, 0) == 'ID':
                continue
            id_names[int(sheet.cell_value(row, 0))] = sheet.cell_value(row, 1)
    elif sheet.name == 'companies':
        for row in range(sheet.nrows):  # it return rows available in sheet
            if sheet.cell_value(row, 0) == 'ID':
                continue
            id_companies[int(sheet.cell_value(row, 0))] = sheet.cell_value(row, 1)

sheet1.write(0, 0, 'ID')
sheet1.write(0, 1, 'Names')
sheet1.write(0, 2, 'Company Name')

for row in range(1, len(id_names.items())):
    id, name = id_names.popitem()
    sheet1.write(row, 0, id)
    sheet1.write(row, 1, name)
    sheet1.write(row, 2, id_companies[id])

create_book.save('Students_new1.xls')