import json


class Usage:
    """ model of a usage """
    json_file = 'data/usages.json'

    def __init__(self):

        # read JSON file
        f = open(self.json_file)
        data = json.load(f)

        # create class variables from data file
        self.usage_dict = data

    def get_label_from_id(self,id):
        return self.usage_dict[str(id)]