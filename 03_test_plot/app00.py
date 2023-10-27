from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
  liste=[]
  for parent, dir_names, file_names in os.walk("mes_fichiers/"):
    for f in file_names :
      filename = os.path.join(parent, f)
      liste.append(filename)
  return render_template("index.html", liste=liste)

# route dynamique
@app.route("/<path:path>")
def fichiers(path):
  contenu = []
  with open(path) as f:
    for line in f:
      contenu.append(line)
  return render_template("contenu.html", path=path, contenu=contenu)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)


