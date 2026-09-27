from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="crud_app"
)

cursor = db.cursor()

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/usuarios")
def view_user():
	cursor.execute("SELECT * FROM usuario")
	users = cursor.fetchAll()
	return render_template("view.user.html", users=users)

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
	if request.method == "POST":
		name = request.form["name"]
		email = request.form["email"]
		phone = request.form["phone"]

		cursor.execute("INSERT INTO usuario (name, email, phone) VALUES (%s, `%s, %s)", (name, email, phone))

		db.commit()
		return redirect(url_for("view_user"))

	return render_template("add_user.html")

if __name__ == "__main__":
	app.run(debug=True)
	
