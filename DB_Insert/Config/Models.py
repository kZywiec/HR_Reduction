from Config.DataBase import db, app
from sqlalchemy.sql import text 
from flask import has_app_context

# Definicja modeli
class Skill(db.Model):
    __tablename__ = 'skills'
    skill_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    skill_name = db.Column(db.String(255), unique=True, nullable=False)

class Applicant(db.Model):
    __tablename__ = 'applicants'
    applicant_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    applicant_name = db.Column(db.String(255), nullable=False)
    industry = db.Column(db.String(255))
    functional_area = db.Column(db.String(255))
    experience = db.Column(db.Integer, nullable=False)
    expected_salary = db.Column(db.Float, nullable=False)

class ApplicantSkill(db.Model):
    __tablename__ = 'applicant_skills'
    applicant_id = db.Column(db.BigInteger, db.ForeignKey('applicants.applicant_id'), primary_key=True)
    skill_id = db.Column(db.BigInteger, db.ForeignKey('skills.skill_id'), primary_key=True)

class JobOffer(db.Model):
    __tablename__ = 'job_offers'
    job_offer_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    job_title = db.Column(db.String(255), nullable=False)
    role_category = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    functional_area = db.Column(db.String(255))
    industry = db.Column(db.String(255))
    salary = db.Column(db.Float, nullable=False)
    required_experience = db.Column(db.Integer, nullable=False)

class JobOfferSkill(db.Model):
    __tablename__ = 'job_offer_skills'
    job_offer_id = db.Column(db.BigInteger, db.ForeignKey('job_offers.job_offer_id'), primary_key=True)
    skill_id = db.Column(db.BigInteger, db.ForeignKey('skills.skill_id'), primary_key=True)

class Application(db.Model):
    __tablename__ = 'applications'
    applicant_id = db.Column(db.BigInteger, db.ForeignKey('applicants.applicant_id'), primary_key=True)
    job_offer_id = db.Column(db.BigInteger, db.ForeignKey('job_offers.job_offer_id'), primary_key=True)



def get_job_offer_details(job_offer_id):
    with app.app_context():
        query = text("SELECT * FROM job_offers WHERE job_offer_id = :job_offer_id")
        result = db.session.execute(query, {"job_offer_id": job_offer_id})
        return [dict(row) for row in result.mappings()]  # Convert to list of dictionaries



def get_required_skills(job_offer_id):
    with app.app_context():
        query = text("""
        SELECT s.skill_name
        FROM job_offer_skills jos
        JOIN skills s ON jos.skill_id = s.skill_id
        WHERE jos.job_offer_id = :job_offer_id
        """)
        result = db.session.execute(query, {"job_offer_id": job_offer_id})
        return [row['skill_name'] for row in result.mappings()]



def get_matching_applicants(job_offer_id):
    with app.app_context():
        query = text("""
        SELECT 
            a.applicant_name, 
            a.experience, 
            a.expected_salary, 
            STRING_AGG(s.skill_name, ', ') AS skill_name
        FROM applications ap
        JOIN applicants a ON ap.applicant_id = a.applicant_id
        JOIN applicant_skills aks ON a.applicant_id = aks.applicant_id
        JOIN skills s ON aks.skill_id = s.skill_id
        WHERE ap.job_offer_id = :job_offer_id
        GROUP BY a.applicant_name, a.experience, a.expected_salary
        """)
        result = db.session.execute(query, {"job_offer_id": job_offer_id})
        return [dict(row) for row in result.mappings()]


