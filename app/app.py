from flask import Flask, jsonify
from google.cloud.datastore import Client
from app import livedate
from data_sources.datastore import DataStore

app = Flask(__name__)
app.register_blueprint(livedate)


def init_datastore(app: Flask, datastore_client: Client, project_id: str):
    app.datastore = DataStore(datastore_client, project_id)


@app.route("/")
def welcome():
    return jsonify({"Message": "hello"}), 200


@app.errorhandler(400)
def error_handler(err: Exception):
    print(f"Bad Request {err.description}")
    return jsonify({"Bad Request": err.description}), 400


@app.errorhandler(404)
def error_handler(err: Exception):
    print(f"Not found {err.description}")
    return jsonify({"Not Found": err.description}), 404


@app.errorhandler(409)
def error_handler(err: Exception):
    print(f"Already exists {err.description}")
    return jsonify({"Already Exists": err.description}), 409


@app.errorhandler(Exception)
def error_handler(err: Exception):
    print(f"I have an error {err}")
    return jsonify({"error": str(err)}), 500


