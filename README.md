# yodaTools
A group of tools I programmed that I use regularly. Public because why not, exists because I was tired of scrolling through repos to copy/paste the same code again and again.
To see examples, check out `examples.py`

Install
=======
Since I didn't want to copy git repos into other projects, I made a pip package
.. code:: shell

    $ pip install yodas

Functions
=========
**camelCaseSplit()**
Input: `str`
Return: `str`

This function takes a string in camel case form and returns it in "normal" form
For example `helloWorld` results in `Hello World`

**snakeCaseSplit()**
Input: `str`
Return: `str`

This function takes a string in snake case form and returns it in "normal" form
For example `hello_world` results in `Hello World`

**caseSplit()**
Input: `str`
Return: `str`

This function takes a string in camel case or snake case form and returns it in "normal" form
For example `helloWorld` and `hello_world` both results in `Hello World`

Classes
=======

Menu
----------------------------------------------------
```python
Menu(items, title=None, subtitle=None, execute=True)
```
This creates a CLI menu based on the inputs.
#### Inputs
1. items `list` (required)
2. title `str`
3. subtitle `str`
4. execute `bool`

**items**
When inputting a `[dictionary]`, it will assume that the key is the title of the object as a string, the value can be any data type, even functions

**title**
If not none, will display everytime `menu.select()` is called.

**subtitle**
If not none, will display everytime `menu.select()` is called.

**execute**
By default it is `True`, if a function is inputted in items, it will automatically execute it when selected

## Usage
```python
>>> from yodas import Menu
>>> menu = Menu(["hello"])`
```
To run the CLI
```python
>>> menu.select()
====================================================================================================
0 : hello

Choose an option: 
```
Inputting `0`, the function `menu.select()` will return `'hello'`
```python
>>> menu.add(exit)
```
adding pythons built-in `exit` to the menu. Running `menu.select()` again.
```python
>>> menu.select()
====================================================================================================
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
To add a custom label, just use a dictionary
```python
>>> menu.add({"Exit Python": exit})
```

###
### select
```python
>>> Menu.select()
```
Will open a CLI interface where the user can select an option
It will return any data type given to upon creating the `Menu` instance
> **returns**: `any`

###
### add
```python
>>> Menu.add(item)
```
See `items` variable in creating a Menu instance. Adds a new item to the menu
> *item:* `any`



Yoda
----
This manages JSON files in a safe manner. When creating an object, the path does not have to exist. If the json file does not exist, Yoda will automatically create one using the `keys` as reference.

For each `key` given upon creation, Yoda will ask the user in a user-friendly manner, what the data is.
## Inputs
> *path:* `str` (required)
> 
> *keys:* `list`

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

###
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
This will overwrite the existing JSON file with the variable `contents`
> *contents*: `dict`

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
2. In Yoda class, add option to have custom questions, similar to what is implemented in Menu()
3. In Menu class, add argument management
4. Fix camelCaseSplit() where `thisIsATest` results in `This Is ATest`
5. Add multiple language support


Changelog
=========

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
