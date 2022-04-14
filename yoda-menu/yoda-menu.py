class Menu:
    """
    This class takes a list of functions to put in a menu

    To specify the function names, each item of the list must be a dictionary
    in the format {"Quit python", exit}
    """
    def __init__(self, menuItems, title=None, subtitle=None):
        self.menuItems = []
        self.title = str(title)
        self.subtitle = subtitle
        for item in menuItems:
            if callable(item):  # Is the menu item a function/callable variable?
                self.menuItems.append(dict({str(item): item}))
            elif type(item) is dict:
                # Dictionary item must be in format
                # {"String", functionVariable}
                self.menuItems.append(item)

        print(self.menuItems)

    def menu(self):
        print("=" * 100)
        if self.title:
            print("\n" + self.title)
        if self.subtitle:
            print("\n" + self.subtitle)

        for i in range(len(self.menuItems)):
            functionName = self.menuItems[i].keys()[0]
            print("{0} : {1}".format(i, functionName))

        # Select option
        option = -1
        try:
            option = int(input("\nChoose an option: "))
        except ValueError:
            print("Not a number :(")
            self.menu()
        except NameError:
            print("Not a number :(")
            return self.menu()

        # Validate
        if 0 <= option <= len(self.menuItems) - 1:
            chosenFunctionName = self.menuItems[option].keys()[0]
            chosenFunction = self.menuItems[option][chosenFunctionName]
        else:
            print("Number out of bounds")
            return self.menu()
        return chosenFunction


def sample1():
    print("Here is where you put the function")


def sample2():
    print("The code works okay, may not be pretty but it works")
    raise Exception("The ugliest code I think i've written")


if __name__ == '__main__':
    options = [{"Quit": exit},
               {"Menu 2": sample1}]
    m = Menu(options, title="Main menu")
    while True:
        m.menu()
