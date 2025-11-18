from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/json")
def home():
    return jsonify({"name": "Ahad", "role": "Developer"})


if __name__ =="__main__":
    app.run(debug=True)