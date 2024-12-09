import os
from datetime import datetime, timedelta
from random import randint

# Configuration
total_day = 596  # nombre total de jours en arrière pour les commits
repo_link = "https://github.com/Grizmite/testproject.git"  # Lien du repo

# Initialisation
now = datetime.now()
pointer = 0
ctr = 1

# Configuration du dépôt
os.system("git config user.name")
os.system("git config user.email")
os.system("git init")

# Boucle pour générer les commits
while total_day > 0:
    current_date = now - timedelta(days=pointer)
    # Exclure les week-ends
    if current_date.weekday() < 5:  # 0 = Lundi, ..., 4 = Vendredi
        commit_count = randint(2, 7)  # Nombre aléatoire de commits entre 2 et 7
        while commit_count > 0:
            # Création d'un commit
            with open("commit.txt", "a+") as f:
                formatdate = current_date.strftime("%Y-%m-%d")
                f.write(f"Commit {ctr}: {formatdate}\n")
            
            os.system("git add .")
            os.system(f"git commit --date=\"{formatdate} 12:15:10\" -m \"Commit {ctr}\"")
            print(f"Commit {ctr}: {formatdate}")
            
            commit_count -= 1
            ctr += 1

    pointer += 1
    total_day -= 1

# Pousser les commits sur le dépôt
os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")
