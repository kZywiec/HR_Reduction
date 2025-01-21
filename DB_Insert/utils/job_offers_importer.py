import csv
from Config.Models import JobOffer, JobOfferSkill, Application
from Config.DataBase import db, app

def import_job_offers(file_path):
    with app.app_context():
        with db.session.begin():
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    job_title = row['job_title'].strip()
                    role_category = row['role_category'].strip()
                    location = row['location'].strip()
                    functional_area = row['functional_area'].strip()
                    industry = row['industry'].strip()
                    salary = float(row['salary'])
                    required_experience = int(row['required_experience'])

                    db.session.merge(JobOffer(
                        job_title=job_title,
                        role_category=role_category,
                        location=location,
                        functional_area=functional_area,
                        industry=industry,
                        salary=salary,
                        required_experience=required_experience
                    ))
    print(f"Dane z {file_path} zostały zaimportowane do tabeli applicant_skills.")
