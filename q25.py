with open('user_input2.txt', 'r') as source_file:
    with open('user_input1.txt', 'w') as destination_file:
        content = source_file.read()
        destination_file.write(content)

print("Contents copied from 'source.txt' to 'destination.txt'")
