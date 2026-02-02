import csv

stats = {}

with open("mes_notes.csv", encoding="latin-1", newline="") as f:
    for r in csv.DictReader(f, delimiter=";"):
        cours = r["Cours"]
        coef = float(r["Coefficient"].replace(",", "."))
        note = float(r["Note"].replace(",", "."))

        if cours not in stats:
            stats[cours] = {"sum": 0.0, "coef": 0.0}

        stats[cours]["sum"] += note * coef
        stats[cours]["coef"] += coef

for cours, v in stats.items():
    print(cours, ":", v["sum"] / v["coef"])
