print(
    list(
        map(
            lambda i: "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i),
            range(0, int(input("Max number: ")))
        )
    )
)
