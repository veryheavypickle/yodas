from src.yodas import *


def menuAsStringsExample():
    stringMenu = Menu(["Test 1", "Test 2"])
    returnedString = stringMenu.select()
    print(returnedString)
    print(type(returnedString))


def yodaExample():
    yodaObject = Yoda("here.json", ["token"])
    print(yodaObject.contents())
    yodaObject.delete()


def utilitiesExample():
    print(caseSplit("helloWorld"))
    print(caseSplit("hello_world"))
    print(caseSplit("thisIsATest"))
    print(caseSplit("this_is_a_test"))


def main():
    menu = Menu([quit,
                 main,
                 {"Example of Yoda Class": yodaExample},
                 utilitiesExample,
                 menuAsStringsExample],
                title="Example Menu")
    while True:
        menu.select()


if __name__ == '__main__':
    main()
