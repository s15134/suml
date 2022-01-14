from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask import request
import pickle
import sklearn as sk
from form import FormInput

app = Flask(__name__)

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

trained_model = "model_creditworthiness.sv"
model = pickle.load(open(trained_model, 'rb'))

# all Flask routes below


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.route('/', methods=['GET'])  # , methods=['GET', 'POST'])
def home():
    title = 'HomePage'
    return render_template('home.html', title=title, now=datetime.utcnow())


@app.route('/about', methods=['GET'])  # , methods=['GET', 'POST'])
def about():
    title = 'About'
    return render_template('about.html', title=title, now=datetime.utcnow())


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = FormInput(request.form)
    title = "Form"
    if request.method == 'POST': 
        if form.validate():
            employment = form.employment.data
            phone_possesing = form.phone_possesing.data
            academic = form.academic.data
            childrens = form.childrens.data
            family = form.family.data
            income = form.income.data
            estate = form.estate.data
            age = form.age.data
            data = [[estate, childrens, income, academic,
                    age, employment, phone_possesing, family]]
            wilgetcredit = model.predict(data)
            s_confidence = model.predict_proba(data)
            ml_respond = ("Czy dana osoba będzie miała problemy ze spłatą zobowiązania? {0}".format(
                "TAK " if wilgetcredit[0] == 1 else "NIE.") + " Prawdopodobieństwo wyniku: {0:.2f} %".format(
                s_confidence[0][wilgetcredit][0] * 100))
            return render_template('about.html', form=form, title=title, now=datetime.utcnow(), ml=ml_respond)
        else:
            return render_template('wrong.html', form=form, title=title)
    return render_template('form.html', form=form, title=title, now=datetime.utcnow())


if __name__ == '__main__':
    app.run(debug=True)
