import json
friends_list = [
    'John','Rambo','Sam',
]
json_format = json.dumps(friends_list)
print(json_format)
print(type(json_format))