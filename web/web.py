import sys
sys.path.append("../utils/")
import service_ports

from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    services = service_ports.services()
    return render_template("service_ports.html", services=services)

@app.route('/services')
def services():
    return jsonify(service_ports.services())

app.run(debug=True, host="0.0.0.0")