# app.py
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"mensagem": "Minha primeira API com Flask no Render!"})


if __name__ == "__main__":
    app.run()
