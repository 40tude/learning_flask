from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Salut</h1>"

# localhost:8080/user/philippe
@app.route('/user/<name>')
def user(name):                         # Pas oublier "name" en paramètre !!!! 
  return (f"<h1>Salut {name}</h1>")

# localhost:8080/safe_user/philippe
@app.route('/safe_user/<name>')
def safe_user(name):
  return (f"<h1>Salut {escape(name)}</h1>")

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)
