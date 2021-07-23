from flask import Flask, jsonify
from metric_scraper import get_families


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def hello_world():
    return jsonify(get_families())