def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nOriginal content successfully read.\n")
    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
        return
    except IOError:
        print("❌ Error: Could not read the file.")
        return

    # Modify the content
    modified_content = modify_content(content)

    # Define a new file name for output
    output_filename = "modified_" + filename

    try:
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"✅ Modified content written to '{output_filename}'.")
    except IOError:
        print("❌ Error: Could not write to the new file.")

if __name__ == "__main__":
    main()