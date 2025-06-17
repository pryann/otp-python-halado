x = "global"


def locale():
    x = "local"
    print(x)


locale()
print(x)


def one(x):
    print(x)

    def two():
        x = 10
        print(x)

        def three():
            print(x)

        return three

    return two


one("one")()()  # prints "one" three times
