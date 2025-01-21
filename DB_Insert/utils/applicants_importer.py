import csv
from Config.Models import Applicant
from Config.DataBase import db, app

def import_applicants(file_path):
    with app.app_context():
        with db.session.begin():
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    applicant_name = row['Name'].strip()
                    industry = row['Industry'].strip()
                    functional_area = row['Functional Area'].strip()
                    experience = int(row['Experience (Years)'])
                    expected_salary = float(row['Expected Salary'])
                    
                    db.session.merge(Applicant(
                        applicant_name=applicant_name,
                        industry=industry,
                        functional_area=functional_area,
                        experience=experience,
                        expected_salary=expected_salary
                    ))
        print(f"Dane z {file_path} zostały zaimportowane do tabeli applicants.")
