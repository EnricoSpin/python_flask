from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>Aprendendo Python e Flask</h1>"

@app.route("/sobre")
def sobre():
	return "<h1>Este é um mini curso sobre Python e Flask</h1>"

@app.route("/contatos")
def contatos():
	return "<h1>Contatos: Eu</h1>"

if __name__ == "__main__":
	app.run(debug=True)
	
