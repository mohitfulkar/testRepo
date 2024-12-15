def display(name):
    seen = set()
    duplicate = set()

    # Identify all duplicate characters
    for char in name:
        if char in seen:
            duplicate.add(char)
        else:
            seen.add(char)

    # Remove all duplicate characters from the original string
    result = ""
    for char in name:
        if char not in duplicate:
            result += char

    print(result)

name = input("Enter your name: ")
display(name)
