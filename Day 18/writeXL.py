import xlwt

book = xlwt.Workbook()
sheet1 = book.add_sheet('Students')
sheet2 = book.add_sheet('Companies')

sheet1.write(0, 0, 'ID')
sheet1.write(0, 1, 'Name')
sheet1.write(1, 0, 1)
sheet1.write(1, 1, 'Jatin')

sheet2.write(0, 0, 'ID')
sheet2.write(0, 1, 'Name')
sheet2.write(1, 0, 1)
sheet2.write(1, 1, 'TCS')

book.save('Students_new.xls')


