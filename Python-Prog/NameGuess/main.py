from flask import Flask,render_template
import requests

app = Flask(__name__)



@app.route("/guess/<name>")
def guess_name(name):
    age1 = requests.get(f"https://api.agify.io/?name={name}").json()['age']
    gender1 = requests.get(f"https://api.genderize.io/?name={name}").json()['gender']
    return render_template("index.html", p_name=name, age=age1, gender=gender1)


if __name__ == "__main__":
    app.run(debug=True)