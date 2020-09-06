#!/bin/bash
pip install virtualenv
virtualenv nutritiondb
source bin/activate
pip install flask
pip install flask-sqlalchemy
python db_creator.py
pip install Flask-WTF
pip install flask_table
