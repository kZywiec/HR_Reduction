import csv
from Config.Models import Skill
from Config.DataBase import db, app

def import_skills(file_path):
    with app.app_context(): 
        with db.session.begin(): 
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    skill_name = row['Skill'].strip().lower()
                    if not Skill.query.filter_by(skill_name=skill_name).first():
                        db.session.merge(Skill(skill_name=skill_name))
        print(f"Dane z {file_path} zostały zaimportowane do tabeli skills.")
