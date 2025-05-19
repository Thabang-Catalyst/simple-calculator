
def process_file():
    filename = input("Enter the name of the file to read (e.g., input.txt): ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            
        # Convert to uppercase
        modified_content = content.upper()

        # Count words
        word_count = len(content.split())

        output_file = input("Enter a name you wan't the new document to be saved as(e.g output.txt): ")
        # Write to a new file
        with open(output_file, 'w') as new_file:
            new_file.write("Modified Content (Uppercase):\n")
            new_file.write(modified_content)
            new_file.write(f"\n\nWord Count: {word_count}\n")

        print("✅ File processed successfully. Check '{output_file}'.")
    
    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    
    except IOError:
        print("❌ Error: Could not read the file. Please make sure it is accessible.")

# Run the program
process_file()
