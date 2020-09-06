# forms.py

from wtforms import Form, StringField, SelectField, validators

class MusicSearchForm(Form):
    choices = [('ImageName', 'ImageName'),
               ('Sugar', 'Sugar'),
               ('Protein', 'Protein')]
    select = SelectField('Search for item:', choices=choices)
    search = StringField('')


class AlbumForm(Form):
    diet_types = [('None', 'None'),
                   ('Vegan', 'Vegan'),
                   ('Halal', 'Halal')
                   ]
    imagename = StringField('ImageName')
    calories = StringField('Calories/100g')
    sugar = StringField('Sugar/100g')
    protein = StringField('Protein/100g')
    diet_type = SelectField('Diet', choices=diet_types)
