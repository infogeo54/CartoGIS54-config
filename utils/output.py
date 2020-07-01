import os
import json


class Output:
    def __init__(self, directory, entrypoint="app.config.json"):
        """
        Create an Output instance by specifying the target
        :param path: String - The output file path
        :param entrypoint: String - The output file name (with extension)
        """
        self.directory = directory
        self.entrypoint = entrypoint
        self.path = "{}/{}".format(directory, entrypoint)
        self.structure = {
            "form": {
                "inputText": [],
                "inputNumber": [],
                "inputDate": [],
                "inputRange": [],
                "textArea": [],
                "selectBox": []
            }
        }

    def add_inputText(self, field):
        inputText_list = self.structure["form"]["inputText"]
        inputText_list.append(field)

    def add_inputNumber(self, field):
        inputNumber_list = self.structure["form"]["inputNumber"]
        inputNumber_list.append(field)

    def add_inputDate(self, field):
        inputDate_list = self.structure["form"]["inputDate"]
        inputDate_list.append(field)

    def add_inputRange(self, field):
        inputRange_list = self.structure["form"]["inputRange"]
        inputRange_list.append(field)

    def add_textArea(self, field):
        textArea_list = self.structure["form"]["textArea"]
        textArea_list.append(field)

    def add_selectBox(self, field):
        selectBox_list = self.structure["form"]["selectBox"]
        selectBox_list.append(field)

    def parse(self):
        return json.dumps(self.structure)

    def save(self):
        parsed_structure = self.parse()
        f = open(self.path, "w")
        f.write(parsed_structure)
        f.close()


