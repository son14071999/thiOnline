import json

with open('thpt_data.json') as json_file:
    data = json.load(json_file)
    print(data)

# a = 'afvdf'
# print(a.index('b'))