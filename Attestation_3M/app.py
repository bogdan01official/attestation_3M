import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DATABASE = "mydatabase.db"

@app.route("/", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Users (username, password) VALUES (?, ?)",
                (username, password),
            )
            conn.commit()
            conn.close()
            return "Запрос успешно отправлен"
        except:
            return "Произошла ошибка во время отправки запроса"
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
