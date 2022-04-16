from .utilities.strings import caseSplit


class Menu:
    """
    This class takes a list of functions or strings to put in a menu

    items
    in the format [{"Quit python", exit}]

    execute
    if true, the menu automatically executes the selected function
    """
    def __init__(self, items, title=None, subtitle=None, execute=True, layout=None):
        assert type(items) is list
        self.items = []
        self.title = title
        self.subtitle = subtitle
        self.execute = bool(execute)

        # Formatting header
        if not layout:
            # Default view
            self.layout = self.setLayout("=" * 50 + "\n%T\n%S")

        # Add items to menu
        for item in items:
            self.append(item)

    def select(self):
        self.__printLayout()

        for i in range(len(self.items)):
            functionName = list(self.items[i].keys())[0]
            print("{0} : {1}".format(i, functionName))

        # Select option
        option = -1
        try:
            option = int(input("\nChoose an option: "))
        except ValueError:
            print("Not a number :(")
            self.select()
        except NameError:
            print("Not a number :(")
            return self.select()

        # Validate
        if 0 <= option <= len(self.items) - 1:
            chosenFunctionName = list(self.items[option].keys())[0]
            chosenFunction = self.items[option][chosenFunctionName]
        else:
            print("Number out of bounds")
            return self.select()

        if self.execute and callable(chosenFunction):
            chosenFunction()
        return chosenFunction

    def setLayout(self, layout):
        """
        This is used to customise the format, similar to 'git log --pretty="%H custom text"'
        %T = Title
        %S = Subtitle
        """
        self.layout = layout
        return self.layout

    def __printLayout(self):
        layout = self.layout

        titleVar = "%T"
        subtitleVar = "%S"
        if self.title and titleVar in self.layout:
            layout = layout.replace(titleVar, self.title)
        else:
            layout = layout.replace(titleVar, "")
        if self.subtitle and subtitleVar in self.layout:
            layout = layout.replace(subtitleVar, self.subtitle)
        else:
            layout = layout.replace(subtitleVar, "")
        print(layout)

    def append(self, item):
        """
        This adds items into the menu
        """
        if callable(item):  # Is the menu item a function/callable variable?
            try:
                name = caseSplit(item.__name__)
                self.items.append({name: item})
            except AttributeError:
                # I will assume it is quit
                self.items.append({"Quit": item})
        elif type(item) is dict:
            # Dictionary item must be in format
            # {"String", functionVariable}
            self.items.append(item)
        else:
            # is string, float, int... etc
            self.items.append({item: item})
        return True

    def pop(self):
        """
        Pops item from menu
        """
        return self.items.pop()

    def remove(self, item):
        """
        Removes specific item from menu items
        """
        try:
            self.items.remove(item)
            return True
        except ValueError:
            return False

    def setExecute(self, execute):
        assert execute is bool
        self.execute = execute
        return True
