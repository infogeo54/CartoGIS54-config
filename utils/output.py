import os


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
