
# with open("file.log", "r") as file:
#     for line in file:
#         if "WARNING" in line:
#             print (line.strip())
    
import time

file_path = "file.log"

with open (file_path, "r") as file:
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep (1)
            continue
        elif "ERROR" in line:
            print ("new error was found in:", line.strip())
            
        elif "WARNING" in line:
            print ("New WARNING message found", line.strip())