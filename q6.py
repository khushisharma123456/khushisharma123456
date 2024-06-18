filename = "output.txt"

with open(filename, "r") as file:
    content = file.read()
    
    # Print the content to the console
print("Content of the file:")
print(content)