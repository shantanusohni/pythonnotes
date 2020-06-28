import xlrd
import xlwt

create_book = xlwt.Workbook()
sheet1 = create_book.add_sheet('Students')

book = xlrd.open_workbook('Students.xlsx') # it creates a workbook object
sheets = book.sheets() # It list all sheets available in workbook

sheet1.write(0, 0, 'ID')
sheet1.write(0, 1, 'Names')
sheet1.write(0, 2, 'Company Name')
for row in range(sheets[1].nrows):
    for col in range(sheets[1].ncols):
        sheet1.write(row, col, sheets[0].cell_value(row, col))
        sheet1.write(row, 2, sheets[1].cell_value(row, 1))

create_book.save('Students_new1.xls')