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
  return render_template("index05.html", liste=liste)



if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)


