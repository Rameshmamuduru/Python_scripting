import shutil
import subprocess
import os

# src_file = r"test/New folder/text.txt.txt"
# target_path = r"E:\Python\test\New folder (2)"

# if not os.path.exists (target_path):
#     os.makedirs (target_path)
# else:
#     shutil.copy (src_file, target_path)
    
    
    
# os.remove (src_file)
# os.rmdir()

#dir = r"E:\Python"

subprocess.run (["ping", "-n", "4", "www.google.com"])
subprocess.run ("ping -n 4 www.google.com", shell=True)