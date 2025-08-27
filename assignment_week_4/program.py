def modify_file_content(content):
    """Convert text to uppercase and count words."""
    word_count = len(content.split())
    processed_text = content.upper()
    return processed_text, word_count


def main():
    # Ask user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Process the file content
        processed_text, word_count = modify_file_content(content)

        # Create a new filename
        new_filename = "modified_" + filename

        # Write processed content to new file
        with open(new_filename, "w") as file:
            file.write(processed_text)
            file.write(f"\n\nWord Count: {word_count}\n")

        print(f"✅ Success! Modified file saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename.")
    except PermissionError:
        print("Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
