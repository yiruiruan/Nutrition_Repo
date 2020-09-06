from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    imagename = Col('ImageName')
    calories = Col('Calories/100g')
    sugar = Col('sugar/100g')
    protein = Col('Protein/100g')
    diet_type = Col('Diet')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))