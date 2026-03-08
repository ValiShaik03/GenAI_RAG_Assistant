from flask import Flask, request, jsonify, render_template
from rag import generate_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.json
    message = data["message"]

    reply = generate_answer(message)

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True)