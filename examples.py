from src.yodas import *


def yodaExample():
    yodaObject = Yoda("here.json", ["token"])
    print(yodaObject.contents())
    yodaObject.delete()


def utilitiesExample():
    print(caseSplit("helloWorld"))
    print(caseSplit("hello_world"))


def main():
    menu = Menu([quit, main, {"Example of Yoda Class": yodaExample}, utilitiesExample])
    menu.show()


if __name__ == '__main__':
    main()
