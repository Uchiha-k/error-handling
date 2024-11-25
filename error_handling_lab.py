filename = input("Enter the name of the file to read: ")

try:
    # Try to open the file
    with open(filename, "r") as file:
        content = file.read()  # Read the file content
        print("File content:")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
