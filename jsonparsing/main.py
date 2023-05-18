import json

with open('sample_data.json') as json_file:
    json_data = json.load(json_file)
print(type)
parameter = json_data["parametersList"]
data_final = []
for data in parameter:
    parameterName = data.get("parameterName")
    max_value = data.get("max")
    min_value = data.get("min")
    avg_value = data.get("avg")
    data_dict = {
        "parameterName": parameterName,
        "max": max_value,
        "min": min_value,
        "avg": avg_value
    }
    data_final.append(data_dict)

json_String = json.dumps(data_final)
with open("json_parsed.json", "w") as json__file:
    json__file.write(json_String)

