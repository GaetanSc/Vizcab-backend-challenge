import json
from model.construction_element import Construction_element

class Zone:
    """ model of a zone """
    json_file = 'data/zones.json'

    def __init__(self,zone_id):

        # read JSON file
        f = open(self.json_file)
        data = json.load(f)

        # create class variables from data file
        self.zone_dict = next((zone for zone in data if zone["id"] == zone_id))
        self.id = zone_id
        self.nom = self.zone_dict["nom"]
        self.surface = self.zone_dict["surface"]
        self.usage = self.zone_dict["usage"]
        self.constructionsElements = self.zone_dict["constructionElements"]


    def get_surface(self):
        return  self.surface

    def get_usage(self):
        return self.usage

    def get_impact_total(self,periodeDeReference):
        """return the sum of the carbon emission impact of every different construction elements, according to the quantity present in this zone

        ret : float"""
        impact_total = 0
        for constructionElement in self.constructionsElements:
            id = constructionElement["id"]
            quantity = constructionElement["quantite"]
            impact_total += quantity * Construction_element(id).get_impact_total(periodeDeReference)

        return impact_total