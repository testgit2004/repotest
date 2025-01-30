from flask import Flask, request
from operations import somme
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculer():
    resultat = ""
    if request.method == "POST":
        try:
            nombre1 = float(request.form["nombre1"])
            nombre2 = float(request.form["nombre2"])
            resultat = f"Le Résultat est : {somme(nombre1,nombre2)}"
        except ValueError:
            resultat = "Erreur : Entrez des nombres valides."
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculateur</title>
    </head>
    <body>
        <h1>Calcul de la somme</h1>
        <form method="POST">
            <label>Premier nombre :</label>
            <input type="text" name="nombre1" required>
            <br><br>
            <label>Deuxième nombre :</label>
            <input type="text" name="nombre2" required>
            <br><br>
            <button type="submit">CALCULER</button>
        </form>
        <h2>{resultat}</h2>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
