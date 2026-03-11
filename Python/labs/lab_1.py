import datetime

# Feature 1 → Read a file and display content
def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()
            print("\n--- File Content ---")
            print(content)
    except FileNotFoundError:
        print("❌ Error: File not found!")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")


# Feature 2 → Write user input into a file
def write_file(file_path, text):
    try:
        with open(file_path, "w") as f:
            f.write(text)
        print("✅ File written successfully!")
    except PermissionError:
        print("❌ Error: You don't have permission to write to this file.")


# Feature 3 → Append logs into a file
def append_log(log_path, message):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_path, "a") as f:
            f.write(f"[{timestamp}] {message}\n")
        print("📝 Log entry added.")
    except PermissionError:
        print("❌ Error: Cannot write log file due to permissions.")


# Simple CLI
if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Read File")
        print("2. Write File")
        print("3. Append Log")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            path = input("Enter file path to read: ")
            read_file(path)

        elif choice == "2":
            path = input("Enter file path to write: ")
            text = input("Enter text to write: ")
            write_file(path, text)

        elif choice == "3":
            log_path = input("Enter log file path: ")
            message = input("Enter log message: ")
            append_log(log_path, message)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("❌ Invalid choice! Please try again.")
