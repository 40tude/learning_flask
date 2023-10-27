from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # definit une route. Ici la route racine
def home():

  # Logique de l'application
  MesDonnees = {
    "user"   :"Philippe",
    "machine": "Linux"
  }
  marcel=18

  # Display de la page correspondant à la route
  return render_template('index.html', marcel, title="Home", data=MesDonnees)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)


