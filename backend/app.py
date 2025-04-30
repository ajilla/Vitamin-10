from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

quotes = [
    "Be yourself; everyone else is already taken.",
    "Two things are infinite: the universe and human stupidity.",
    "So many books, so little time.",
    "A room without books is like a body without a soul."
]

@app.route("/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)
