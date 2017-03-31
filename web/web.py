import sys
sys.path.append("../utils/")
import service_ports

from flask import Flask
from flask import render_template
from flask import jsonify
from flask import make_response

app = Flask(__name__)

@app.route('/')
def home():
    services = service_ports.services()
    return render_template("service_ports.html", services=services)

@app.route('/services')
def services():
    resp = make_response(jsonify(service_ports.services()))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

app.run(debug=True, host="0.0.0.0")