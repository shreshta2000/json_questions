import json
new_data = {}
data =    '{"a":  1,"a":  2,"a":  3, "a": 4,"b": 1,"b": 2}'
convert = json.loads(data)
for i in convert:
    for j in convert:
        if i in j :
            new_data[j] = convert[j]
print(new_data)
