def open_file():
    with open("ListSquare.py", "r") as file:
        content = file.read()
        print(content)



open_file()