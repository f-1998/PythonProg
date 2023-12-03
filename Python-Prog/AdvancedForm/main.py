from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email, ValidationError, InputRequired
from flask_bootstrap import Bootstrap4


class LoginForm(FlaskForm):
    email = EmailField(label='Email:', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    submit = SubmitField('Log In')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'
bootstrap = Bootstrap4(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        pword = login_form.password.data
        if email == 'admin@email.com' and pword == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
