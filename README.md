```
                   __                     
                  /\ \                    
 __  __    ___    \_\ \     __      ____  
/\ \/\ \  / __`\  /'_` \  /'__`\   /',__\ 
\ \ \_\ \/\ \L\ \/\ \L\ \/\ \L\.\_/\__, `\
 \/`____ \ \____/\ \___,_\ \__/.\_\/\____/
  `/___/> \/___/  \/__,_ /\/__/\/_/\/___/ 
     /\___/                               
     \/__/
```
A group of tools I programmed that I use regularly. Public because why not, exists because I was tired of scrolling through repos to copy/paste the same code again and again.
To see examples, check out `examples.py`

### Projects that use yodas
1. [IOSBackupExtractor](https://github.com/veryheavypickle/iOSBackupExtractor)

Install
=======
Since I didn't want to copy git repos into other projects, I made a pip package
```shell
$ pip install yodas
```

Functions
=========
###
### camelCaseSplit
```python
>>> from yodas import camelCaseSplit
>>> camelCaseSplit(string)
```
This function takes a string in camel case form and returns it in "normal" form
For example `helloWorld` results in `Hello World`
> *string:* `str`
> 
> **returns:** `str`

### snakeCaseSplit
```python
>>> from yodas import snakeCaseSplit
>>> snakeCaseSplit(string)
```
This function takes a string in snake case form and returns it in "normal" form
For example `hello_world` results in `Hello World`
> *string:* `str`
> 
> **returns:** `str`

### caseSplit
```python
>>> from yodas import caseSplit
>>> caseSplit(string)
```
This function takes a string in camel case or snake case form and returns it in "normal" form
For example `helloWorld` and `hello_world` both results in `Hello World`
> *string:* `str`
> 
> **returns:** `str`

Classes
=======

Menu
----------------------------------------------------
This creates a CLI menu based on the inputs.
## Inputs
```python
from yodas import Menu
Menu(items, title=None, subtitle=None, execute=True, layout=None)
```
> *items:* `list` (required)
> 
> *title:* `str`
> 
> *subtitle:* `str`
> 
> *execute:* `bool`
> 
> *layout:* `str`
> 
> **returns:** `Menu`

**items**
When inputting a `[dictionary]`, it will assume that the key is the title of the object as a string, the value can be any data type, even functions

**title**
If not none, will display everytime `menu.select()` is called.

**subtitle**
If not none, will display everytime `menu.select()` is called.

**execute**
By default it is `True`, if a function is inputted in items, it will automatically execute it when selected

**layout**
This is a string that customises the appearance of the menu.

## Usage
```python
>>> from yodas import Menu
>>> menu = Menu(["hello"])
```
To run the CLI
```python
>>> menu.select()
====================
0 : hello

Choose an option: 
```
Inputting `0`, the function `menu.select()` will return `'hello'`
```python
>>> menu.append(exit)
```
appending pythons built-in `exit` to the menu. Running `menu.select()` again.
```python
>>> menu.select()
====================
0 : hello
1 : Quit

Choose an option: 
```
Selecting `1` results in executing `exit()` automatically. To stop automatically running functions
```python
>>> menu.setExecute(False)
```
This can also be setup upon menu creation
```python
>>> menu = Menu([exit, "hello"], execute=False)
```
To append a custom label, just use a dictionary
```python
>>> menu.append({"Exit Python": exit})
```

## Functions
### select
```python
>>> Menu.select()
```
Will open a CLI interface where the user can select an option
It will return any data type given to upon creating the `Menu` instance
> **returns**: `any`

###
### append
```python
>>> Menu.append(item)
```
See `items` variable in creating a Menu instance. Appends a new item to the menu. Returns bool on whether operation was successful
> *item:* `any`
> 
> **returns:** `bool`

###
### pop
```python
>>> Menu.pop()
```
Pops the last item from the list of menu items. Returns the item removed
> *item:* `any`
> 
> **returns:** `any`

###
### remove
```python
>>> Menu.remove(item)
```
Removes a specific item from the menu list. Will return True if operation was successful, returns False if item doesn't exist
> *item:* `any`
> 
> **returns:** `bool`

###
### setExecute
```python
>>> Menu.setExecute(execute)
```
Sets the auto execute on the menu which dictates whether functions should be automatically executed when it is selected. Returns bool on whether operation was successful
> *execute:* `bool`
> 
> **returns**: `bool`

###
### setLayout
This customises the appearance of the menu. By default, it is `"=" * 50 + "\n%T\n%S"`.
```python
>>> menu.setLayout(layout)
```
When `subtitle is None`, `title = "Menu"` and `layout = "=" * 5 " %T " + "=" * 5` results in the appearance of.
```
===== Menu =====
0 : First menu Item
1 : 2nd Item
```
When `subtitle is None`, `title = "Menu"` and `layout = %T` results in the appearance of.
```
Example Menu
0 : First menu Item
1 : 2nd Item
```
> *layout:* `string`
> > %T is `title`
> 
> > %S is `subtitle`

Yoda
----
This manages JSON files in a safe manner. When creating an object, the path does not have to exist. If the json file does not exist, Yoda will automatically create one using the `keys` as reference.

For each `key` given upon creation, Yoda will ask the user in a user-friendly manner, what the data is.
## Inputs
```python
from yodas import Yoda
Yoda(path, keys=[])
```
> *path:* `str` (required)
> 
> *keys:* `list`
> 
> **returns:** `Yoda`

**path**
This is the path to the JSON file

**keys**
This is a list of keys that will be in the JSON file. If the JSON file does not exist, Yoda will ask the user to fill out the JSON file based on the provided keys.
This is used by me personally to write scripts that require authentication.
For example in telegram, I don't want to have my first commits to have the telegram token.

## Usage
To implement a Yoda object
```python
>>> from yodas import Yoda
>>> yoda = Yoda("file.json", ["ping!"])
```

Executing this will result in
```
For each key, give its required value
ping!: 
```

Entering `pong!` will save it to the JSON file. To check this, run
```python
>>> yoda.contents()
{'ping!': 'pong!'}
```

To doublecheck this
```shell
$ cat file.json
{
    "ping!": "pong!"
}% 
```
## Functions
### contents
```python
>>> Yoda.contents()
```
Will return the contents of the JSON file, reading from the disk everytime.
> **returns:** `dict`

###
### write
```python
>>> Yoda.write(contents)
```
This will overwrite the existing JSON file with the variable `contents`. Returns `bool` if the operation was successful.
> *contents:* `dict`
> 
> **returns:** `bool`

###
### delete
```python
>>> Yoda.delete()
```
Will delete the JSON file associated with the Yoda instance. Returns True if it was successful, False if nothing was deleted.
> **returns:** `bool`

###
### getPath
```python
>>> Yoda.getPath()
```
Is used to get the path where the JSON file is stored.
> **returns:** `str`

###
### setPath
```python
>>> Yoda.setPath(path)
```
This used to set the path
> *path:* `str`


TODO
====
1. In Yoda class, add option to have other variables like a `key: list`, or `key: dict` rather than just `str: str`
2. In Yoda class, add option to have custom questions rather than just reading keys
3. In Menu class, add argument management
4. Fix `camelCaseSplit()` where `thisIsATest` results in `This Is ATest`

Changelog
=========

1.4.0
-----
Adding more insight into the inner workings of `Menu`

1. Added `Menu.setLayout(laout)` which customises the appearance of the Menu
2. Changed `Menu.add(item)` to `Menu.append(item)`
3. Added new function `Menu.pop()`
4. Added new function `Menu.remove(item)`
5. Fixed format issue in `README`

1.3.1
-----
Adding return variables to all functions.

1. Majorly reformatted README.md
2. `Yoda.delete()` now returns `bool` depending on whether the operation was successful or not.
3. `Yoda.__setPath()` now returns `bool` if successful
4. `Yoda.write()` returns `bool` 
5. `Menu.setExecute()` returns `bool`
6. `Menu.add()` returns `bool`

1.3.0
-----
1. Major update to README.md
2. In Yoda() changed name of function `open()` to `__open()`
3. In Yoda() changed name of function `setPath()` to `__setPath()`
4. In Menu() added new function `setExecute()`

1.2.0
-----
1. Added full support to store items other than functions
2. In Menu() added support to add new items after menu creation using Menu.add()
3. In Menu() moved code to add items to Menu.add()

1.1.1
-----
1. Added support to create empty Yoda `Yoda("empty.json")` will create a JSON with `{}`
2. Fixed issue where even in empty Yoda files, it will ask for the details

1.1.0
-----
1. Added support for string only menus
2. Changed Menu.show() to Menu.select()
3. Fixed issue where camelCaseSplit() wouldn't detect words with a length of 2
4. Fixed issue whereupon creating Yoda, it won't ask for details until contents() is called
5. Fixed issue in Yoda where if the path doesn't exist, Yoda will crash
