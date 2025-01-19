import csv
from Config.Models import JobOffer, JobOfferSkill, Application
from Config.DataBase import db, app


def import_job_offers(file_path):
    with app.app_context():
        with db.session.begin():
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    job_title = row['Job Title'].strip()
                    role_category = row['Role Category'].strip()
                    location = row['Location'].strip()
                    functional_area = row['Functional Area'].strip()
                    industry = row['Industry'].strip()
                    salary = float(row['Salary'])
                    required_experience = int(row['Required Experience'])

                    db.session.add(JobOffer(
                        job_title=job_title,
                        role_category=role_category,
                        location=location,
                        functional_area=functional_area,
                        industry=industry,
                        salary=salary,
                        required_experience=required_experience
                    ))
        print(f"Data from {file_path} has been imported into the job_offers table.")