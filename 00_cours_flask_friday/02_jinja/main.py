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


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)
