# """
# Juice Maker
#
# You are given a Juice class, which has name and capacity properties.
# You need to complete the code to enable and adding of two Juice objects,
# resulting in a new Juice object with the combined capacity and names
# of the two juices being added.
#
# For example, if you add an Orange juice with 1.0 capacity
# and an Apple juice with 2.5 capacity, the resulting juice should have:
# name: Orange&Apple
# capacity: 3.5
#
# The names have been combined using an & symbol.
# Use the __add__ method to define a custom behavior
# for the + operator and return the resulting object.
# """
#
#
# class Juice:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity
#
#     def __str__(self):
#         return self.name + " (" + str(self.capacity) + "L)"
#
#     def __add__(self, other):
#         return f"{self.name}&{other.name} ({self.capacity + other.capacity}L)"
#
#
# a = Juice('Orange', 1.5)
# b = Juice('Apple', 2.0)
#
# result = a + b
# print(result)
#
#
# def function():
#     print("Module function!")
#
#
# if __name__ == "__main__":
#     print("Script")
#
# def concatenate(*args):
#     output = ""
#     for item in args:
#         output += item + " "
#     output = output.strip(" ").replace(" ", "-")
#     return output
#
#
# print(concatenate("I", "love", "Python", "!"))
#
# txt = input().split(" ")
#
# print(max(txt, key=len))
#
# num = int(input())
#
#
# def fibonacci(n):
#     if n in {0, 1}:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for number in range(num):
#     print(fibonacci(number))
#
# for bathroom in range(5, int(input()) + 1, 5):
#     print(bathroom)
#
text = input()
word = input()


def search(given_text, given_word):
    if given_text.__contains__(given_word):
        return "Word found"
    else:
        return "Word not found"


print(search(text, word))
