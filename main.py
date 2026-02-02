import csv

stats = {} # On déclare un dictionnaire plus simple pour les données

with open("mes_notes.csv", encoding="latin-1", newline="") as f:
    for r in csv.DictReader(f, delimiter=";"): # Lecture ligne par ligne du CSV, csv.DictReader permet de lire la première ligne comme en-tête
        # Extraction des champs (manipulable avec des variables)
        cours = r["Cours"] 
        coef = float(r["Coefficient"].replace(",", "."))
        note = float(r["Note"].replace(",", "."))
        semestre = r["Semestre"]

        if semestre not in stats: # Si le semestre n'éxiste pas encore --> On créer un dictionnaire vide
            stats[semestre] = {}

        if cours not in stats[semestre]:
            stats[semestre][cours] = {"sum": 0.0, "coef": 0.0} # Chaque cours stock le total de note + coef

        stats[semestre][cours]["sum"] += note * coef
        stats[semestre][cours]["coef"] += coef

for semestre, cours_2 in stats.items(): # Parcour des resultats
    print(semestre, "\n")
    for cours, v in cours_2.items(): # Parcour uniquement les cours dans le semestre actuelle et v vaut sum et coef
        print(cours, ":", v["sum"] / v["coef"]) 
