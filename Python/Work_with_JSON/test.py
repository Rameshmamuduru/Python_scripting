import json

file_path = r"E:\Python\Work_with_JSON\file.json"

try:
    with open(file_path, "r") as file:
        config = json.load(file)
    #print(config)
except FileNotFoundError:
    print("Error: 'file.json' not found.")
except json.JSONDecodeError:
    print("Error: 'file.json' contains invalid JSON.")
    

print("App Name:", config["app_name"])
print("Version:", config["version"])

# Nested values
print("DB Host:", config["data_base"]["host"])
print("DB Port:", config["data_base"]["port"])

# List values
print("Features:", ", ".join(config["features"]))
