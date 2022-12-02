from flask import Flask,render_template, request, flash, url_for

app=Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key="emperor"

@app.route("/")
def index():
    flash("what is your name?")
    return render_template("app.html")

@app.route("/welcome", methods=["POST","GET"])
def welcome():
    flash('Welcome '+ str(request.form["name_input"]+" !"))
    flash('Bienvenue '+ str(request.form["name_input"]+" !"))
    flash('ようこそ '+ str(request.form["name_input"]+" !"))
    flash('Willkommen '+ str(request.form["name_input"]+" !"))
    return render_template("app.html")

if __name__ == "__main__":
    app.run()
