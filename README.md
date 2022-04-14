# yodaTools
A group of tools I programmed that I use regularly. Public because why not, exists because I was tired of scrolling through repos to copy/paste the same code again and again.


## Yoda
This is used by me personally to write scripts that require authentication.
For example in telegram, I don't want to have my first commits to have the telegram token.

using this as an example, to create a valid json file on the spot with the required keys I just run
`>>> yodaObject = Yoda("tokens.json", ["token"])`
`>>> yodaObject.contents()` to print out the contents

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
m = Menu(options, title="Main menu")
while True:
    f = m.menu()
    f()
```

Since I didn't want to copy git repos into other projects, I made a pip package
`$ pip install yodas`

## TODO
1. in Yoda class, add option to have other variables like a key: list, or key: dict
