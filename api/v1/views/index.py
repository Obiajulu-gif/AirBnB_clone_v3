#!/usr/bin/python3
"""
starts a Flask web application
"""

from api.v1.views import app_views
from flask import Flask, jsonify
app = Flask(__name__)
app.url_map.strict_slashes = False


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
