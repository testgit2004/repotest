from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calcul_formulaire_web():
    resultat = ""
    if request.method == "POST":
        try:
            nombre1 = float(request.form["nombre1"])
            nombre2 = float(request.form["nombre2"])
            url = "http://127.0.0.1:5000/calcul"
            response = requests.post(url, json={"a": nombre1, "b": nombre2})
            if response.status_code == 200:
                data = response.json()
                resultat = f"Résultat : {data['resultat']}"
            else:
                data = response.json()
                resultat = f"Erreur : {data.get('erreur', 'Erreur inconnue.')}"
        except ValueError:
            resultat = "Erreur : Entrez des nombres valides."

    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculateur</title>
    </head>
    <body>
        <h1>Calculateur de Somme</h1>
        <form method="POST">
            <label>Premier nombre :</label>
            <input type="text" name="nombre1" required>
            <br><br>
            <label>Deuxième nombre :</label>
            <input type="text" name="nombre2" required>
            <br><br>
            <button type="submit">Calculer</button>
        </form>
        <h2>{resultat}</h2>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
