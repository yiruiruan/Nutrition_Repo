# Image/Nutrition_Repo

Build with: Python, Flask, SQL, HTML

This can be used to find nutrition information about a specific type of food and help with having a good diet.

Available Functionalities: Add, Edit, View, and Search (currently displays the entire database)

Instructions to setup on Linux based Machines:
1. Go to imgrepo folder
2. To setup the environment, run bash setup.sh
3. To spin up the repo, Run FLASK_APP=main.app flask run

(* if it has sqlalchemy issues, try running python db_creator.py and redo step 3).

*the current search function is only implemented to find all results given no input value*
