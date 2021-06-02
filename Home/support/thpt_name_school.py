# Reading an excel file using Python
import xlrd
import json
# Give the location of the file
loc = (r"D:\pycharm\django\thiOnline\Home\support\4._dm_truong_thpt_2019v2.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

rows = sheet.nrows
cols = sheet.ncols
f = open('thpt.txt', 'w', encoding='UTF-8')
for row in range(rows):
    schools = sheet.cell_value(row, 6).replace("\n", ' ').strip()
    if schools != '' and schools != 'Tên Trường':
        print(schools)
        f.write(schools+"\n")
f.close()



# print(len(provinces))

