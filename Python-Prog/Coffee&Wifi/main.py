from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

COFFEE_CHOICES = ['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️', '✘']
WIFI_CHOICES = ['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪', '✘']
POWER_CHOICES = ['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌', '✘']

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message="Cafe name cannot be empty.")])
    location = StringField('Location', validators=[DataRequired(), URL(message="Invalid URL.")])
    open = StringField('Open', validators=[DataRequired(message="Opening hours cannot be empty.")])
    closing = StringField('Close', validators=[DataRequired(message="Closing hours cannot be empty.")])
    coffee = SelectField(choices=COFFEE_CHOICES, validators=[DataRequired()])
    wifi = SelectField(choices=WIFI_CHOICES, validators=[DataRequired()])
    power = SelectField(choices=POWER_CHOICES, validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_cafe = [form.cafe.data, form.location.data, form.open.data,
                        form.closing.data, form.coffee.data, form.wifi.data, form.power.data]
            with open('cafe-data.csv', newline='', mode='a', encoding='utf-8') as fp:
                writer = csv.writer(fp)
                writer.writerow(new_cafe)
            return redirect('cafes')
    return render_template('add.html', form=form)



@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        first_row = list_of_rows[0]
        list_of_rows.remove(first_row)
    return render_template('cafes.html', cafes=list_of_rows, frow=first_row)


if __name__ == '__main__':
    app.run(debug=True)
