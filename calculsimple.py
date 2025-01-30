import requests

def calcul_console():
    try:
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
        url = "http://127.0.0.1:5000/calcul"
        response = requests.post(url, json={"a": a, "b": b})
        if response.status_code == 200:
            print("Résultat :", response.json()["resultat"])
        else:
            print("Erreur :", response.json().get("erreur", "Erreur inconnue."))
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    except requests.RequestException as e:
        print(f"Erreur réseau : {e}")

if __name__ == "__main__":
    calcul_console()
