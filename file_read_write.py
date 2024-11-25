try:
    # Open a file for reading
    with open("input.txt", "r") as infile:
        content = infile.read()  # Read the file content
    
    # Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()
    
    # Write the modified content to a new file
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("File processed successfully. Check 'output.txt' for results.")

except FileNotFoundError:
    print("Error: The file 'input.txt' does not exist.")
