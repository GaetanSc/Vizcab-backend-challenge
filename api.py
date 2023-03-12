from flask import *
from controller.batiment import batiments


app = Flask(__name__)
app.register_blueprint(batiments, url_prefix='/batiments')


@app.route('/', methods=['GET'])
def home():
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and "static" not in rule.rule:
            links.append(rule.rule)

    return links


if __name__ == "__main__":

    app.run(debug=True)

