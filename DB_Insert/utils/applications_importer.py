import csv
from Config.Models import JobOffer, JobOfferSkill, Application
from Config.DataBase import db, app

def import_applications(file_path):
    with app.app_context():
        with db.session.begin():
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    applicant_id = int(row['applicant_id'])
                    job_offer_id = int(row['job_offer_id'])

                    db.session.merge(Application(
                        applicant_id=applicant_id,
                        job_offer_id=job_offer_id
                    ))
    print(f"Dane z {file_path} zostały zaimportowane do tabeli applicant_skills.")
