from flask import render_template, Flask, redirect, request, url_for

app = Flask(__name__)

messages = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message")
        messages.append(message)
        return redirect(url_for("index"))
    return render_template("index.html", messages=messages)


if __name__ == "__main__":
    app.run()
