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
        self.structure = {
            "server": {
                "host": "",
                "queryParams": []
            },
            "form": {
                "inputText": [],
                "inputNumber": [],
                "inputDate": [],
                "inputRange": [],
                "textArea": [],
                "selectBox": []
            },
            "modals": []
        }

    def path(self):
        return "{}/{}".format(self.directory, self.entrypoint)

    def categories(self):
        return self.structure["form"]
    
    def fields(self):
        res, categories = [], self.categories()
        for c in categories:
            res.extend(categories[c])
        return res

    def field(self, name):
        for f in self.fields():
            if f["name"] == name:
                return f
        return

    def add_inputText(self, config):
        self.categories()["inputText"].append(config)

    def add_inputNumber(self, config):
        self.categories()["inputNumber"].append(config)

    def add_inputDate(self, config):
        self.categories()["inputDate"].append(config)

    def add_inputRange(self, config):
        self.categories()["inputRange"].append(config)

    def add_textArea(self, config):
        self.categories()["textArea"].append(config)

    def add_selectBox(self, config):
        self.categories()["selectBox"].append(config)
    
    def add_config(self, config):
        """
        Add a field's config to the appropriate section, depending on it's type
        :param config: Dict - A field's config
        :return Void
        """
        t, o = config["type"], config["options"]
        if t == "TextEdit":
            if "IsMultiline" in o:
                if o["IsMultiline"]:
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
        """
        Extract layers' configs then add each one of them on the the appropriate section
        :param layers: List - Current projects' layers
        """
        for c in layers_configs(layers):
            self.add_config(c)

    def save(self):
        """
        Parse structure into json then create the output file and write inside
        """
        parsed_structure = json.dumps(self.structure)
        f = open(self.path(), "w+")
        f.write(parsed_structure)
        f.close()


