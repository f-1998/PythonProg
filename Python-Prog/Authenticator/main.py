from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
bcrypt = Bcrypt(app)


# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email=request.form.get("email")
        res = User.query.filter_by(email=email).first()
        if res:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        new_user = User(
        email = request.form.get("email"),
        name = request.form.get("name"),
        password = bcrypt.generate_password_hash(request.form.get("password")).decode('utf-8'),
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return render_template('secrets.html', name=new_user.name)
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email entered.
        the_object = User.query.filter_by(email=email).first()
        if not the_object:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not bcrypt.check_password_hash(the_object.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(the_object)
            return redirect(url_for('secrets'))
    return render_template("login.html")



@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory('static/files', 'cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
