def read_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if not line:
            break
        lines.append(line)
    return lines

def main():
    print("Enter multiple lines. Press Enter on an empty line to finish.")
    user_lines = read_lines()

    if user_lines:
        print("\nYou entered the following lines:")
        for line in user_lines:
            print(line)
    else:
        print("No lines were entered.")

if __name__ == "__main__":
    main()
