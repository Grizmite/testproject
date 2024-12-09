import os
from datetime import datetime, timedelta
from random import randint, random

# Configuration
total_day = 596  # nombre total de jours en arrière pour les commits
repo_link = "https://github.com/Grizmite/testproject.git"  # Lien du repo

# Initialisation
now = datetime.now()
pointer = 0
ctr = 1

# Initialiser le dépôt Git
os.system("git config user.name 'Grizmite'")
os.system("git config user.email 'chaberjb@hotmail.com'")
if not os.path.exists(".git"):
    os.system("git init")

# Ajouter ou mettre à jour le remote
os.system("git remote remove origin || true")  # Supprime l'existant si nécessaire
os.system(f"git remote add origin {repo_link}")

# Boucle pour générer les commits et branches/PR
while total_day > 0:
    current_date = now - timedelta(days=pointer)
    # Exclure les week-ends
    if current_date.weekday() < 5:  # 0 = Lundi, ..., 4 = Vendredi
        commit_count = randint(2, 7)  # Nombre aléatoire de commits entre 2 et 7
        
        if random() <= 0.3:  # 30 % de chance de créer une PR
            branch_name = f"branch-{pointer}"
            os.system(f"git checkout -b {branch_name}")  # Crée une nouvelle branche

            while commit_count > 0:
                with open("commit.txt", "a+") as f:
                    formatdate = current_date.strftime("%Y-%m-%d")
                    f.write(f"Commit {ctr}: {formatdate}\n")
                os.system("git add .")
                os.system(f"git commit --date=\"{formatdate} 12:15:10\" -m \"Commit {ctr}\"")
                print(f"Commit {ctr}: {formatdate}")
                commit_count -= 1
                ctr += 1

            os.system(f"git push -u origin {branch_name}")  # Pousse la branche
            # Crée une Pull Request via gh CLI
            os.system(f"gh pr create --title 'Auto-generated PR for {branch_name}' --body 'This PR merges {branch_name} into main.' --base main")

        else:  # 70 % de chance de faire des commits normaux sur la branche main
            os.system("git checkout main")  # Assurez-vous d'être sur la branche main
            while commit_count > 0:
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

# Pousser la branche principale
os.system("git checkout main")
os.system("git push -u origin main -f")
