# Reading an excel file using Python
import xlrd
import json
# Give the location of the file
loc = (r"D:\pycharm\django\thiOnline\Home\support\4._dm_truong_thpt_2019v2.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

rows = sheet.nrows
cols = sheet.ncols
provinces = []
towns = []
results = []
for row in range(rows):
    province = sheet.cell_value(row, 2).replace("\n", ' ').strip()
    if province != ''and province != 'Tên Tỉnh/TP':
        if province not in provinces:
            provinces.append(province)
            results.append({
                'name': str(province),
                'towns': []
            })
        town = sheet.cell_value(row, 4).replace("\n", ' ').strip()
        if town not in towns:
            towns.append(town)
            for i in range(len(results)):
                if results[i]['name'].replace("\n", ' ').strip() == province:
                    results[i]['towns'].append({
                        'name': town,
                        'schools': []
                    })

        school = sheet.cell_value(row, 6).replace("\n", ' ').strip()
        try:
            school = school[0:school.index('(')].strip()
        except :
            pass
        for i in range(len(results)):
            if results[i]['name'].replace("\n", ' ').strip() == province:
                for j in range(len(results[i]['towns'])):
                    if results[i]['towns'][j]['name'] == town:
                        results[i]['towns'][j]['schools'].append(school)
                        break


print(len(results))
with open('thpt_data.json', 'w') as outfile:
    json.dump(json.dumps(results, ensure_ascii=False, indent=2), outfile)


# print(len(provinces))

