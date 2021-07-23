from flask import Flask, jsonify
from metric_scraper import fetch_families, get_families


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

fetch_families()

@app.route("/")
def hello_world():
    return jsonify(get_families())