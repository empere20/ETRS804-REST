from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class CalculPrix(Resource):
    def get(self):
        km = request.args.get('km')
        devise = request.args.get('devise')
        prix = 0.25 * float(km)
        if devise == "euro":
            prix = 0.88* prix
        elif devise == "livre":
            prix = 0.76 * prix
        elif devise == "rouble":
            prix = 73.96 * prix
        elif devise == "yen":
            prix = 102.58 * prix
        elif devise == "yuan":
            6.94 * prix
        dico = {'Prix': prix}
        return jsonify(dico)


api.add_resource(CalculPrix, '/')

"""if __name__ == '__main__':
    app.run(debug=True)"""