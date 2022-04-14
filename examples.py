from src.yodas import *


def printJson():
    print(jsonFile)


def main():
    menu = Menu([quit, main, {"Print JSON": printJson}])
    menu.show()


if __name__ == '__main__':
    # Load json
    yodaObject = Yoda("here.json", ["token"])
    jsonFile = yodaObject.contents()
    main()
