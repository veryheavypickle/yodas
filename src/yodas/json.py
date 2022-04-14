import json


class JSON:
    """
    This class takes a path to a JSON file and loads its contents.
    If the JSON file doesn't exist, it will construct the yodas file, save it and still get the required contents

    For some reason I was running this in python 2.7, note that it does not work in 2.7
    """
    def __init__(self, path, valueTitles):
        self.path = path
        self.valueTitles = valueTitles  # used for when the JSON doesn't exist and constructs a yodas with these values

    def contents(self):
        contents = self.openJSON()
        if contents == {}:
            contents = self.__createJSON()
        return contents

    def __createJSON(self):
        titles = self.valueTitles
        contents = {}
        print("For each of the keys below, paste the value")
        for title in titles:
            try:
                value = str(input("{}: ".format(title)))
            except NameError:
                print("You are not running python 3!")
            contents[title] = value

        self.writeJSON(contents)
        return contents

    def openJSON(self):
        path = self.getPath()
        try:
            jsonFile = open(path)
            file = json.load(jsonFile)
            jsonFile.close()
            return file
        except IOError:
            if ".yodas" not in path:  # try opening the yodas file with .yodas
                self.setPath(path + ".yodas")
                return self.openJSON()
            else:
                return {}
        except ValueError:
            return {}

    def writeJSON(self, contents):
        assert type(contents) is dict
        path = self.getPath()
        jsonFile = open(path, "w")
        json.dump(contents, jsonFile, indent=4)
        jsonFile.close()

    def getPath(self):
        return self.path

    def setPath(self, path):
        self.path = path

