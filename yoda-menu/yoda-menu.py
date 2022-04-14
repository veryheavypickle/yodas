def menuOptions(optionsList, title=None, subtitle=None, validate=True):
    print("\n")
    if subtitle is not None:
        print("\n" + subtitle)
    if title is not None:
        print("\n" + title)
    print("=" * 100)
    backText = "Menu/Quit"
    optionsList.insert(0, backText)
    for i in range(len(optionsList)):
        print("{0} : {1}".format(i, optionsList[i]))
    optionsList.pop(0)
    try:
        option = int(input("\nChoose an option: "))
    except Exception as e:
        print("\nOh no, that ain't a number, cowboy")
        print(e)
        option = -1
    if 0 <= option <= len(optionsList) or not validate:  # checks if option is within range
        if option == 0:
            if title == "Main Menu":
                exit()
            else:
                menu()
        else:
            return int(option - 1)
    else:
        print("\nThat option doesn't seem to be available :(")
        return menuOptions(optionsList, title=title, validate=validate)


def menu(error=None):
    options = ["Menu 1",
               "Menu 2"]
    while True:
        option = menuOptions(options, title="Main Menu", subtitle=error)
        if option == 0:
            print("Here is where you put the function")
        elif option == 1:
            print("The code works okay, may not be pretty but it works")
        error = None  # this is so the error doesn't show up again in the menu after it was triggered


menu()