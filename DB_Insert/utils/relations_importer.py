import csv
from Config.Models import ApplicantSkill
from Config.DataBase import db, app

def import_applicant_skills(file_path):
    with db.session.begin():
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                applicant_id = int(row['applicant_id'])
                skill_id = int(row['skill_id'])

                if not ApplicantSkill.query.filter_by(applicant_id=applicant_id, skill_id=skill_id).first():
                    db.session.add(ApplicantSkill(applicant_id=applicant_id, skill_id=skill_id))
    print(f"Dane z {file_path} zostały zaimportowane do tabeli applicant_skills.")
