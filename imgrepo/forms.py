# forms.py

from wtforms import Form, StringField, SelectField, validators

class MusicSearchForm(Form):
    choices = [('ImageName', 'ImageName'),
               ('Album', 'Album'),
               ('Publisher', 'Publisher')]
    select = SelectField('Search for music:', choices=choices)
    search = StringField('')


class AlbumForm(Form):
    media_types = [('Digital', 'Digital'),
                   ('CD', 'CD'),
                   ('Cassette Tape', 'Cassette Tape')
                   ]
    imagename = StringField('ImageName')
    title = StringField('Title')
    release_date = StringField('Release Date')
    publisher = StringField('Publisher')
    media_type = SelectField('Media', choices=media_types)
