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
            "form": {
                "inputText": [],
                "inputNumber": [],
                "inputDate": [],
                "inputRange": [],
                "textArea": [],
                "selectBox": []
            }
        }

    def get_path(self):
        return "{}/{}".format(self.directory, self.entrypoint)

    def get_categories(self):
        return self.structure["form"]
    
    def get_fields_count(self):
        count = 0
        categories = self.get_categories()
        for c in categories:
            count += len(categories[c])
        return count
    
    def get_fields(self):
        fields = []
        categories = self.get_categories()
        for c in categories:
            fields.extend(categories[c])
        return fields

    def find_field_by_name(self, name):
        fields = self.get_fields()
        for f in fields:
            if f["name"] == name:
                return f
        return

    def add_inputText(self, config):
        inputText_list = self.get_categories()["inputText"]
        inputText_list.append(config)

    def add_inputNumber(self, config):
        inputNumber_list = self.get_categories()["inputNumber"]
        inputNumber_list.append(config)

    def add_inputDate(self, config):
        inputDate_list = self.get_categories()["inputDate"]
        inputDate_list.append(config)

    def add_inputRange(self, config):
        inputRange_list = self.get_categories()["inputRange"]
        inputRange_list.append(config)

    def add_textArea(self, config):
        textArea_list = self.get_categories()["textArea"]
        textArea_list.append(config)

    def add_selectBox(self, config):
        selectBox_list = self.get_categories()["selectBox"]
        selectBox_list.append(config)
    
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
        configs = layers_configs(layers)
        for c in configs:
            self.add_config(c)


    def save(self):
        """
        Parse structure into json then create the output file and write inside
        """
        parsed_structure = json.dumps(self.structure)
        f = open(self.get_path(), "w+")
        f.write(parsed_structure)
        f.close()


