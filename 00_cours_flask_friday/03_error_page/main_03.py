# https://jinja.palletsprojects.com/en/3.1.x/
# Voir les filtres : https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters
# On peut passer list, dictionnaires...

 
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

'''
safe : 
evite l'injection de code si on veut passer du HTML.
jinja par défaut vire le HTML
Dans l'exemple faut mettre le filtre safe pour afficher le texte en gras

striptags:
Enlève les tags html
Peut être utile si un user laisse un message en injectant du html 
On peut vouloir tout virer, garder que le texte

title : première lettre en majuscule
capitalize : tout en 
lower
upper
trim : enlève les espaces
'''

@app.route('/')
def index():
  first_name = "Philippe"
  stuff = "This is <strong>bold</strong> text"

  lst_pizzas = [
    "pizza 1",
    "pizza 2",
    "pizza 3",
    42
  ]
  return render_template("index.html", first_name=first_name, stuff=stuff, lst_pizzas=lst_pizzas)

@app.route('/user/<name>')
def user(name):                         # Pas oublier "name" en paramètre !!!! 
  return render_template("user.html", user_name=name)

# Custom error pages
# Invalid URL
# http://localhost:8080/bob.html par exemple
@app.errorhandler(404)
def page_not_found(e):
  # TO DO : vérifier cette histoire de ,404 à la fin
  return render_template("404.html"), 404 


# Internal Error Server
@app.errorhandler(500)
def page_not_found(e):
  return render_template("500.html"), 500 

# Pour git en CLI voir à partir de 6:00
# https://youtu.be/3O4ZmH5aolg?si=5PiU6JQzHWqfDe_J

# Version control par projet
# Sortir de l'environnement virtuel Python si y en a un (deactivate)

# Dans le home créer répertoire .ssh mkdir .ssh
# Aller dans ce réperoire et ssh-keygen.exe
# ENTER aux 3 questions posées
# ls, on doit voir id_rsa.pub
# ouvrir et copier son contenu (cat)

# Aller sur github et ajouter la clé publique au compte
# Cliquer profil en haut à droite
# Settings dans la liste
# A gauche de la page chercher SSH & GPG
# Clic bouton New SSH Key
# Coller la clé publique
# Redonner notre password et c'est bon pour github

# Retourner dans le répertoire du projet
# Si y a un sous répertoire ./venv faut pas le pousser sur github
# touch .gitignore
# ajouter les 2 lignes, sauver k
# .gitignore
# virt/

# Rentrer dans l'environnement virtuel si y en a un
# https://python.land/virtual-environments/virtualenv
# venv\Scripts\Activate.ps1

# Setup version control. Si toute 1er fois => toutes les lignes sinon la dernière
# git config --global user.name "Your Name"
# git config --global user.email "you@youraddress.com"
# git config --global push.default matching
# git config --global alias.co checkout
# git init

# git add .
# git commit -am "initial commit"

# Setup a repo sur GitHub
# Github
# Repo
# New Repo
# Donner un nom
# Voir sur la page les 3 lignes pour pusher
# git remote add origin ...
# git branch -M main            (le prompt change de master à main. Des conneries sociales...)
# git push -u origine main

# Répondre Y à la question
# On est bon on peut voir le code sur Github

# On fait un changement sur un source
# Pour pusher sur github => 3 lignes
# git add .
# git commit -am "Un message"
# git push
# On retrouve le changement sur github
# Sur le fichier modifier on peut cliquer sur history
# On voit les différents commits







if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)
