# yodaTools
A group of tools I programmed that I use regularly. Public because why not, exists because I was tired of scrolling through repos to copy/paste the same code again and again.
To see examples, check out examples.py in the git repository

## Yoda
This is used by me personally to write scripts that require authentication.
For example in telegram, I don't want to have my first commits to have the telegram token.

using this as an example, to create a valid json file on the spot with the required keys I just run

`>>> yodaObject = Yoda("tokens.json", ["token"])`

`>>> yodaObject.contents()` to print out the contents of the json file

## Menu
This is a menu thing I wrote actually years ago, looking at the code for the menu now it is absolutely disgusting
Any unhandled errors that occur will have a traceback tree the size of the distance between here and andromeda.

Like the latest commit I copied the menu code from was in March 2017.

One day I will optimise it and on that day you will get an unhandled ErectionError the size of the distance I mentioned earlier but in microns

Okay so I fixed it slightly
Menu is now a class
```
options = [{"Quit": exit},
           {"Menu 2": sample1}]
menu = Menu(options, title="Main menu")
while True:
    menu.get()
```

Since I didn't want to copy git repos into other projects, I made a pip package
`$ pip install yodas`

## Structure

### Functions
#### camelCaseSplit()
#### snakeCaseSplit()
#### caseSplit()

### Classes
#### Menu
#### Yoda

## TODO
1. In Yoda class, add option to have other variables like a `key: list`, or `key: dict` rather than just `str: str`
2. In Yoda class, add option to have custom questions, similar to what is implemented in Menu()
3. In Menu class, add argument management
4. Fix camelCaseSplit() where `thisIsATest` results in `This Is ATest`
5. Add multiple language support

## Changelog
### 1.1.1
1. Added support to create empty Yoda `Yoda("empty.json")` will create a JSON with `{}`
2. Fixed issue where even in empty Yoda files, it will ask for the details

### 1.1.0
1. Added support for string only menus
2. Changed Menu.show() to Menu.select()
3. Fixed issue where camelCaseSplit() wouldn't detect words with a length of 2
4. Fixed issue whereupon creating Yoda, it won't ask for details until contents() is called
5. Fixed issue in Yoda where if the path doesn't exist, Yoda will crash
