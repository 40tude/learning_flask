from flask import Flask
app = Flask(__name__)

@app.route("/") # definit une route. Ici la route racine
def home():
  # C'est carrément merdique de faire un return avec le code de la page...
  return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My home page à moi</title>
</head>
<body>
  <h1>Salut à tous</h1  
</body>
</html>
'''


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)


