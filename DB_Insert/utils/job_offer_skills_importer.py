import csv
from Config.Models import JobOffer, JobOfferSkill, Application
from Config.DataBase import db, app


def import_job_offer_skills(file_path):
    with app.app_context():
        with db.session.begin():
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    job_offer_id = int(row['Job Offer ID'])
                    skill_id = int(row['Skill ID'])

                    db.session.add(JobOfferSkill(
                        job_offer_id=job_offer_id,
                        skill_id=skill_id
                    ))
        print(f"Data from {file_path} has been imported into the job_offer_skills table.")
