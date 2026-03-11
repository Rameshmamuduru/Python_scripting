def count_words(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()

        # Counting logic
        lines = content.splitlines()
        words = content.split()
        characters = len(content)

        print("\n----- Word Count Result -----")
        print(f"Total Lines     : {len(lines)}")
        print(f"Total Words     : {len(words)}")
        print(f"Total Characters: {characters}")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist!")
        
count_words (r"E:\bean\vprofile-project\pom.xml")