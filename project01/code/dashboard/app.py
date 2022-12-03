from flask import Flask
from flask import render_template
import subprocess

app = Flask(__name__)

proc = -1

@app.route("/")
def index():
    return render_template("control_panel.html")

@app.route("/on")
def on():
    global proc
    if proc == -1:
        proc = subprocess.Popen(["python3", "./dht22.py"])
    return render_template("control_panel.html")

@app.route("/off")
def off():
    global proc
    if proc != -1:
        proc.kill()
        proc = -1
    return render_template("control_panel.html")

if __name__ == "__main__":
    try:
        app.run(host="192.168.137.15", port=5000, debug=True)
    except Keyboardinterrupt:
        pass
    finally:
        if proc != -1:
            proc.kill()
            proc = -1

