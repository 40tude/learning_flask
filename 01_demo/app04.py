from flask import Flask, render_template
import platform
import netifaces # https://www.programcreek.com/python/example/81895/netifaces.interfaces
import winreg as wr

app = Flask(__name__)

def get_connection_name_from_guid(iface_guids):
  iface_names = ['(unknown)' for i in range(len(iface_guids))]
  reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
  reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
  for i in range(len(iface_guids)):
      try:
          reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'\Connection')
          iface_names[i] = wr.QueryValueEx(reg_subkey, 'Name')[0]
      except FileNotFoundError:
          pass
  return iface_names


@app.route("/") # definit une route. Ici la route racine
def home():

  # Logique de l'application
  interface_names = get_connection_name_from_guid(netifaces.interfaces())
  MesDonnees = {
    "user"   :"Philippe",
    "machine": platform.node(),
    "os" : platform.system(),
    "dist" : platform.win32_ver(),
    "interfaces" : interface_names
  }

  # Display de la page correspondant à la route
  return render_template('index04.html', title="Home", data=MesDonnees)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)


