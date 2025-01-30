from tkinter import *
import requests

def calculer():
    try:
        a = float(entry_nombre1.get())
        b = float(entry_nombre2.get())
        url = "http://127.0.0.1:5000/calcul"
        response = requests.post(url, json={"a": a, "b": b})
        if response.status_code == 200:
            resultat = response.json()["resultat"]
            label_resultat.config(text=f"Résultat : {resultat}")
        else:
            erreur = response.json().get("erreur", "Erreur inconnue.")
            label_resultat.config(text=f"Erreur : {erreur}")
    except ValueError:
        label_resultat.config(text="Erreur : Entrez des nombres valides.")
    except requests.RequestException as e:
        label_resultat.config(text=f"Erreur réseau : {e}")

fenetre = Tk()
fenetre.title("Calculateur")
fenetre.geometry("300x200")

Label(fenetre, text="Premier nombre :").pack()
entry_nombre1 = Entry(fenetre)
entry_nombre1.pack()

Label(fenetre, text="Deuxième nombre :").pack()
entry_nombre2 = Entry(fenetre)
entry_nombre2.pack()

Button(fenetre, text="Calculer", command=calculer).pack()
label_resultat = Label(fenetre, text="")
label_resultat.pack()

fenetre.mainloop()
