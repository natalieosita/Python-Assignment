def read_and_write_file():
    try:
        # Prompt user for the filename to read
        input_filename = input("Enter the name of the file to read: ")

        # Open the file in read mode
        with open(input_filename, 'r') as input_file:
            content = input_file.readlines()

        # Modify the content (e.g., capitalize all lines)
        modified_content = [line.upper() for line in content]

        # Specify the name for the new file
        output_filename = "modified_" + input_filename

        # Write the modified content to the new file
        with open(output_filename, 'w') as output_file:
            output_file.writelines(modified_content)

        print(f"File has been successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename.")
    except IOError:
        print("Error: Unable to read the file. Please ensure it is accessible.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the function
read_and_write_file()