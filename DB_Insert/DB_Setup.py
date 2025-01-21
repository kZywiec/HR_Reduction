from Config.DataBase import app
from utils.skills_importer import import_skills
from utils.applicants_importer import import_applicants
from utils.applicant_skills_importer import import_applicant_skills
from utils.job_offers_importer import import_job_offers
from utils.applications_importer import import_applications
from utils.job_offer_skills_importer import import_job_offer_skills

# Importowanie danych
with app.app_context():
    import_skills('Data/Skills.csv')
    import_applicants('Data/Applicants.csv')
    import_job_offers('Data/Job_offers.csv')
    import_applications('Data/Applications.csv')
    import_applicant_skills('Data/Applicants_Skills.csv')
    import_job_offer_skills('Data/Job_offer_Skills.csv')

if __name__ == '__main__':
    app.run(debug=True)
