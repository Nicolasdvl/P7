from flask import (
    render_template,
    Flask,
    request,
    url_for,
    jsonify,
    make_response,
)
from app.bot import Bot

app = Flask(__name__)
bot = Bot()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/handle_message", methods=["POST"])
def save_message():
    data = request.json
    result = bot.is_it_a_place(data["message"])
    response = make_response(jsonify(result), 200)
    return response


if __name__ == "__main__":
    app.run(debug=True)