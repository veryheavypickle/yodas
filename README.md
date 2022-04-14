# yodaTools
A group of tools I programmed that I use regularly. Public because why not, exists because I was tired of scrolling through repos to copy paste the same code again and again.


## json
I use this sometimes, I am too lazy to explain it for now but it is simple

## menu
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
