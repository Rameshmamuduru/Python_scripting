import os


def list_recursive(path, indent=0):
    items = os.listdir(path)
    print (path)

    for item in items:
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            print("  " * indent + f"File: {item}")
        else:
            print("  " * indent + f"Folder: {item}")
            list_recursive(full_path, indent + 1)   # Enter inside folder

list_recursive(r"E:\Python", indent=0)