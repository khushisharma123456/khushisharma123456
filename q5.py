name = str(input("enter "))
filename= result.txt
with open(filename, "w") as file:
    file.write(name)

print("The string has been written")
