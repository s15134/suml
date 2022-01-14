from flask_wtf import Form
from wtforms import BooleanField, IntegerField, SelectField, RadioField, SubmitField, validators, ValidationError


class FormInput(Form):

    employment = IntegerField("Lata zatrudnienia klineta",[validators.NumberRange(min=0, max=40)])
    phone_possesing = BooleanField("Posiadanie telefonu przez klienta")
    academic = SelectField("Posiadane wykształcenie klienta", choices=[(0, "Wyższe magisterskie"), (1, "Wyższe licencjackie"),
                                                                       (2, "Wykształcenie nieukończone wyższe"), (3, "Wykształcenie średnie"), (4, "Wykształcenie zawodowe")], default=4)
    childrens = IntegerField("Liczba dzieci klienta na utrzymaniu", [validators.NumberRange(min=0, max=10)])
    family = IntegerField("Liczba członków rodziny klienta", [validators.NumberRange(min=0, max=10)])
    income = IntegerField("Roczny dochód klienta" , [validators.NumberRange(min=0, max=400000)])
    age = IntegerField("Wiek klienta")
    estate = BooleanField("Posiadanie nieruchomości przez klienta")
    submit = SubmitField("Sprawdź wypłacalność")
