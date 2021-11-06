file_name = "output.txt"

try:
    with open(file_name) as f:
        file = open(file_name, "w")
        file.write("Test 1\n")

        print("First read")
        file = open(file_name, "r")
        print(file.read())

        file = open(file_name, "w")
        file.write("Test 2\n")

        print("Second read")
        file = open(file_name, "r")
        print(file.read())

        file = open(file_name, "a")
        file.write("Test 3")

        print("Third read")
        file = open(file_name, "r")
        print(file.read())
finally:
    file.close()
