from flask import Flask, request, jsonify

app = Flask(__name__)

# Ma logique de base pour le calcul
def somme(a, b):
    return a + b

# API  pour tous les clients

@app.route("/calcul", methods=["POST" , "GET" ,])
def calcul_api():

    # je récupère les données envoyées par les clients

    data = request.get_json()
    if not data or "a" not in data or "b" not in data:
        return jsonify({"erreur": "Données manquantes"}), 400
    try:
        a = float(data["a"])
        b = float(data["b"])
        return jsonify({"resultat": somme(a, b)})
    except ValueError:
        return jsonify({"erreur": "Veuillez entrer des nombres valides."}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
