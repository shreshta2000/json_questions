import json
with open('data.json') as f:
  convert = json.load(f)

print(convert)