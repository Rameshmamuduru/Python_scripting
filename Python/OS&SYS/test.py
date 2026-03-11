import os
import time

dir_path = r"E:\Python\test_folder"


# Create directory if it doesn't exist

if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    print(f"Directory created: {dir_path}")
else:
    print(f"Directory already exists: {dir_path}")

print("\nStarting folder watcher... Press CTRL + C to stop\n")


# FULL LOOP

while True:
    files = os.listdir(dir_path)
    print(f"Files in {dir_path}:")

    # If folder is empty → create a file
    if not files:
        file_path = os.path.join(dir_path, "my_file.txt")

        with open(file_path, "w") as my_file:
            my_file.write("This is a file created from python script")

        print("File created:", file_path)

    else:
        # List files
        for f in files:
            full_path = os.path.join(dir_path, f)
            if os.path.isfile(full_path):
                print(f"File: {f}")
            else:
                print(f"Folder: {f}")

    print("-" * 40)
    time.sleep(3)   # Wait 3 seconds and repeat
