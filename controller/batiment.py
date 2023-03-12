from flask import Blueprint
from model.batiment import Batiment


batiments = Blueprint('Batiments', __name__)
@batiments.route('/<int:id>/surface')
def get_surface(id):
    batiment = Batiment(id)
    if batiment == None:
        return str("Ce batiment n'existe pas")

    else :
        return [batiment.get_surface()]


@batiments.route('/<int:id>/usage')
def get_usage(id):
    batiment = Batiment(id)
    if batiment == None:
        return str("Ce batiment n'existe pas")

    else:
        return [batiment.get_usage()]


@batiments.route('/<int:id>/impact')
def get_impact(id):
    batiment = Batiment(id)
    if batiment == None:
        return str("Ce batiment n'existe pas")

    else:
        return [batiment.get_impact_total()]