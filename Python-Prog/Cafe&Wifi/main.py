from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

#docmentation of api
#https://api.postman.com/collections/31653862-e09d311b-6982-466e-b1f7-e614ad1190a9?access_key=PMAT-01HH2CT6FFFT93DKKEHWDTHES9

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })


@app.route("/all")
def get_all_cafes():
    cafes = Cafe.query.all()
    cafe_data = [
        {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,

        }
        for cafe in cafes
    ]

    # Return the data as JSON
    return jsonify(cafes=cafe_data)

@app.route("/search")
def find_cafe():
    query_location = request.args.get("loc")
    cafes = Cafe.query.all()
    filtered_cafes = [cafe for cafe in cafes if cafe.location == query_location]
    cafe_data = [
        {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,

        }
        for cafe in filtered_cafes
    ]

    # Return the data as JSON
    return jsonify(cafes=cafe_data)


# HTTP POST - Create Record
'''
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),

    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
'''

# HTTP PUT/PATCH - Update Record
from flask import jsonify, abort

@app.route('/update/<int:id>', methods=["PATCH"])
def update_price(id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.get_or_404(id)

    if cafe:
        cafe.coffee_price = new_price
        try:
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify(error={"Database Error": str(e)}), 500
    else:
        # 404 = Resource not found
        return jsonify(error={"Not Found": f"Sorry, a cafe with id {id} was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route('/delete/<int:id>', methods=["DELETE"])
def delete_cafe(id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretKey":
        cafe = Cafe.query.get_or_404(id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403



if __name__ == '__main__':
    app.run(debug=True)
