from model.zone import Zone
from model.usage import Usage
import json



class Batiment:
    """ model of a batiment """
    json_file = 'data/batiments.json'

    def __init__(self, batiment_id):

        #read JSON file
        f = open(self.json_file)
        data = json.load(f)

        #create class variables from data file
        self.batiment_dict = next((batiment for batiment in data if batiment["id"] == batiment_id))
        self.id = batiment_id
        self.nom = self.batiment_dict["nom"]
        self.surface = self.batiment_dict["surface"]
        self.zoneIds = self.batiment_dict["zoneIds"]
        self.usage = self.batiment_dict["usage"]
        self.periodeDeReference = self.batiment_dict["periodeDeReference"]



    def get_surface(self):
        """return the sum of the surface of each zone

        ret : int"""
        surface_totale = 0

        for zoneId in self.zoneIds:
            surface_totale += Zone(zoneId).get_surface()

        return surface_totale

    def get_usage(self):
        """return the label of the use of the different zones of the building, if the zone have different uses, the use
        of the zone with the biggest surface is chosen


        ret : str"""
        biggest_zone = -1
        usage = None

        for zoneId in self.zoneIds:
            zone = Zone(zoneId)
            if usage!= zone.get_usage() and biggest_zone < zone.get_surface():
                usage = zone.get_usage()
                biggest_zone = zone.get_surface()

        return Usage().get_label_from_id(usage)

    def get_impact_total(self):
        """return the sum of the total carbon impact of each zone

        ret : float """
        impact_total = 0

        for zoneId in self.zoneIds:
            zone = Zone(zoneId)
            impact_total += zone.get_impact_total(self.periodeDeReference)

        return impact_total