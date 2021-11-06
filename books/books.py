file = open("books.txt", "r")

# your code goes here
with open("books.txt", "r") as f:
    lines = f.readlines()
    for i in lines:
        i = i.replace("\n", "")
        print(i[0] + str(len(i)))

file.close()
