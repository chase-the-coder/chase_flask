from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered?')
    mood = RadioField('please choose your mood:',
                      choices=[('mood_one', 'Happy')])
    food_choice = SelectField('pick your food:', choices=[('chi', 'chicken')])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        return redirect(url_for('thankyou'))
    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)