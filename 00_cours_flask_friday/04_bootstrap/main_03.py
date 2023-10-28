from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

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

# http://localhost:8080/bob.html par exemple
@app.errorhandler(404)
def page_not_found(e):
  # TO DO : vérifier cette histoire de ,404 à la fin
  return render_template("404.html"), 404 

# Internal Error Server
@app.errorhandler(500)
def page_not_found(e):
  return render_template("500.html"), 500 

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)



# CDN : content delivery network
# Bootstrap fonctionne
# Navbar
# Aller sur le site
# component, navbar, coller le code
# templates/navbar.html
# coller le code
# ajouter directive include dans base.html
# on relance
# ATTENTION 
# on peut pas mettre de directive {% block content %} ou autre dans commentaires html
# Voir data-bs-theme="dark" dans navbar.html
# Modification de navbar.html (tout est commenté)
# Ajout des liens dans la navbar avec url_for tag : 
# href="{{ url_for('index') }}" faut ' et ' autour de index
# changer le lien "link" de la navbar vers user profile
# Z! page dynamique
# On va pointer sur /user/Philippe par défaut. 
# Faut passer "Philippe"
# href="{{ url_for('user', name='Philippe')}}"





# Code intial de base.html
# <h1>Above</h1>  
# {% block content %}
#     {# Template to be inserted here #}
# {% endblock%}
# <h1>Above</h1>    
