import yaml

file_path = r"E:\Python\work_with_YAML\file.yml"

with open (file_path, "r") as file:
    data = yaml.safe_load (file)
    
print (data)