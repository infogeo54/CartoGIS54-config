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
        self.server = dict(
            host="", 
            queryParams=[]
        )
        self.form = dict(
            inputText=[],
            inputNumber=[],
            inputDate=[],
            inputRange=[],
            textArea=[],
            selectBox=[]
        )
        self.modals = []
        

    def path(self):
        return "{}/{}".format(self.directory, self.entrypoint)

    def set_host(self, host):
        self.server["host"] = host

    def set_query_params(self, query_params):
        self.server["query_params"] = query_params

    def add_query_param(self, query_param):
        self.server["queryParams"].append(query_param)
    
    def fields(self):
        res, categories = [], self.form
        for c in categories:
            res.extend(categories[c])
        return res

    def field(self, name):
        for f in self.fields():
            if f["name"] == name:
                return f
        return

    def add_inputText(self, config):
        self.form["inputText"].append(config)

    def add_inputNumber(self, config):
        self.form["inputNumber"].append(config)

    def add_inputDate(self, config):
        self.form["inputDate"].append(config)

    def add_inputRange(self, config):
        self.form["inputRange"].append(config)

    def add_textArea(self, config):
        self.form["textArea"].append(config)

    def add_selectBox(self, config):
        self.form["selectBox"].append(config)
    
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

    def generate_form(self, layers):
        """
        Extract layers' configs then add each one of them on the the appropriate section
        :param layers: List - Current projects' layers
        """
        for c in layers_configs(layers):
            self.add_config(c)

    def structure(self):
        return dict(
            server=self.server,
            form=self.form,
            modals=self.modals
        )

    def save(self):
        """
        Parse structure into json then create the output file and write inside
        """
        parsed_structure = json.dumps(self.structure())
        f = open(self.path(), "w+")
        f.write(parsed_structure)
        f.close()


