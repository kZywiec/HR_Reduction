from Config.DataBase import app
from utils.skills_importer import import_skills
from utils.applicants_importer import import_applicants
from utils.relations_importer import import_applicant_skills

# Importowanie danych
with app.app_context():
    import_skills('Data/Skills.csv')
    import_applicants('Data/Applicants.csv')
    import_applicant_skills('Data/Applicants_Skills.csv')

if __name__ == '__main__':
    app.run(debug=True)
