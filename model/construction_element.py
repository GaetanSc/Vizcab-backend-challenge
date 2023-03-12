import json


class Construction_element:
    """ model of a construction element """
    json_file = 'data/construction_elements.json'

    def __init__(self, construction_element_id):

        #read JSON file
        f = open(self.json_file)
        data = json.load(f)

        #create class variables from data file
        self.construction_element_dict = next((construction_element for construction_element in data if construction_element["id"] == construction_element_id))
        self.id = construction_element_id
        self.nom = self.construction_element_dict["nom"]
        self.unite = self.construction_element_dict["unite"]
        self.impactUnitaireRechauffementClimatique = self.construction_element_dict["impactUnitaireRechauffementClimatique"]
        self.production = self.impactUnitaireRechauffementClimatique["production"]
        self.construction = self.impactUnitaireRechauffementClimatique["construction"]
        self.exploitation = self.impactUnitaireRechauffementClimatique["exploitation"]
        self.finDeVie = self.impactUnitaireRechauffementClimatique["finDeVie"]
        self.dureeVieTypique = self.construction_element_dict["dureeVieTypique"]

    def get_impact_total(self,periodeDeReference):
        """ calculates the the total unitary impact of carbon emmission of the construction elements

        the variable Rp depends on the Reference Periode, that depends on the building that we have to bring in this function

        periodeDeReference : int
        ret : float"""
        impact_total = 0

        #production
        impact_total += self.production
        #construction
        impact_total += self.exploitation
        #exploitation
        Rp = max(1,periodeDeReference/self.dureeVieTypique)
        impact_total += Rp*self.exploitation+(Rp-1)*(self.construction+self.production + self.finDeVie)
        #finDeVie
        impact_total += self.finDeVie

        return impact_total

