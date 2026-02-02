import csv

with open("mes_notes.csv", encoding="latin-1", newline="") as f:
    for r in csv.DictReader(f, delimiter=";"):
        coef = float(r["Coefficient"].replace(",", "."))
        note = float(r["Note"].replace(",", "."))
        print(r["Cours"], coef, note)


# Il vas falloir créer deux variables, si elles sont identiques, alors on vas pouvoirs calculer et ajouter les coef, sinon on continue à lire


