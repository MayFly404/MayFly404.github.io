from flask import Flask, render_template, request

app = Flask(__name__)

# Home
@app.route('/')
def index():
  return render_template("index.html")

# Cyberhounds Red Site
@app.route('/cybered')
def cyberHoundsRed():
  return render_template("cyberRed.html")


app.run(host='0.0.0.0', port=8080)