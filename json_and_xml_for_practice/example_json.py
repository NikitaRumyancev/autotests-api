import json


dct1 = {
    "name": "Nikita",
    "age": 25,
    "position":
    ["QA", "middle_qa"]
}
print(dct1, type(dct1))
str_json = json.dumps(dct1, indent=True)
print(str_json, type(json))

json_dct = json.loads(str_json)
print(json_dct)

with open("json_file.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

print(data)

with open("json_file.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=True, indent=4)


with open("json_file.json", "r", encoding="utf-8") as file:
    data1 = json.load(file)
    data1 = json.dumps(data1, indent=4)

print(data1, type(data1))