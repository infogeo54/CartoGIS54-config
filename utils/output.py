import os
import json
from .form import layers_configs


class Output:
    def __init__(self, directory):
        """
        Create an Output instance by specifying the target
        :param directory: String - The output file destination
        """
        self.directory = directory
        self.entrypoint = "app.config.json"
        self.path = "{}/{}".format(directory, self.entrypoint)
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

    def add_inputText(self, config):
        inputText_list = self.structure["form"]["inputText"]
        inputText_list.append(config)

    def add_inputNumber(self, config):
        inputNumber_list = self.structure["form"]["inputNumber"]
        inputNumber_list.append(config)

    def add_inputDate(self, config):
        inputDate_list = self.structure["form"]["inputDate"]
        inputDate_list.append(config)

    def add_inputRange(self, config):
        inputRange_list = self.structure["form"]["inputRange"]
        inputRange_list.append(config)

    def add_textArea(self, config):
        textArea_list = self.structure["form"]["textArea"]
        textArea_list.append(config)

    def add_selectBox(self, config):
        selectBox_list = self.structure["form"]["selectBox"]
        selectBox_list.append(config)

    def parse(self):
        return json.dumps(self.structure)
    
    def add_config(self, config):
        f, t, o = config["field"], config["type"], config["options"]
        if t == "TextEdit":
            if "IsMultiline" in o:
                return self.add_textArea(config)
            return self.add_inputText(config)
        if t == "ValueMap":
            return self.add_selectBox(config)
        if t == "Range":
            if o["Style"] == "Slider":
                return self.add_inputRange(config)
            return self.add_inputNumber(config)
        if t == "DateTime":
            return self.add_inputDate(config)

    def generate_structure(self, layers):
        configs = layers_configs(layers)
        for c in configs:
            self.add_config(c)

    def save(self):
        parsed_structure = self.parse()
        f = open(self.path, "w+")
        f.write(parsed_structure)
        f.close()


