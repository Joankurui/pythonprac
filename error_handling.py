def process_file_with_error_handling():
    """
    prompts the user for a file name, attempts to read the file content,modifies it,
    writes the modified content to a new file, and handles errors gracefully.
    """

    while True:
        filename = input("Enter the file name to read: ")
        try:    
            # file Read & write challange:Read the content of the file
            with open(filename, 'r') as f_read:
                original_content = f_read.read()
                print(f"Successfully read from {filename}'.")

                # simulate modifying the content
                modified_content = original_content.upper()  # Example modification
                print("Content modified (eg.,converted to uppercase).")

                new_filename = f"modified_{filename}"
                # file Write & write challange:Write the modified content to a new file
                with open(new_filename, 'w') as f_write:
                    f_write.write(modified_content)
                    print(f"Successfully wrote modified  content written to '{new_filename}'.")   
                    break  # Exit the loop if successful
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.")    
        except IOError as e:
            print(f"Error: Could not read or write file '{filename}'.Details: {e}")  
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
        # call the function to run the program
if __name__ == "__main__":
    process_file_with_error_handling()
    