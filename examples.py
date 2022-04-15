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


def createEmptyYoda():
    yodaObject = Yoda("empty.json")
    print("Yoda contents:\n{0}".format(yodaObject.contents()))
    yodaObject.delete()


def utilitiesExample():
    print(caseSplit("helloWorld"))
    print(caseSplit("hello_world"))
    print(caseSplit("thisIsATest"))
    print(caseSplit("this_is_a_test"))


def main():
    yodaObject = Yoda("test.json", ["ping!"])
    menu = Menu([quit,
                 main,
                 {"Example of Yoda Class": yodaExample},
                 utilitiesExample,
                 menuAsStringsExample,
                 createEmptyYoda,
                 {"Storing object in menu": yodaObject}],
                title="Example Menu")
    while True:
        foo = menu.select()
        if isinstance(foo, Yoda):
            print(foo.contents())
            foo.delete()


if __name__ == '__main__':
    main()
