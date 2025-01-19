from Config.DataBase import app
from utils.skills_importer import import_skills
from utils.applicants_importer import import_applicants
from utils.relations_importer import import_applicant_skills
from utils.relations_importer import import_job_offer_skills
from utils.applications_importer import import_applications
from utils.job_offers_importer import import_job_offers

# Importowanie danych
with app.app_context():
    import_skills('Data/Skills.csv')
    import_applicants('Data/Applicants.csv')
    import_applicant_skills('Data/Applicants_Skills.csv')
    import_job_offer_skills('Data/Job_Offer_Skills.csv')
    import_applications('Data/partial_match_applications.csv')
    import_job_offers('Data/Job_Offers.csv')

if __name__ == '__main__':
    app.run(debug=True)
