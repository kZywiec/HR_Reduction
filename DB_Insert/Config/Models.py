from Config.DataBase import db

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

# Job Offer Model
class JobOffer(db.Model):
    __tablename__ = 'job_offer'
    job_offer_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    job_title = db.Column(db.String(255), nullable=False)
    role_category = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    functional_area = db.Column(db.String(255))
    industry = db.Column(db.String(255))
    salary = db.Column(db.Float, nullable=False)
    required_experience = db.Column(db.Integer, nullable=False)

# Job Offer Skills Model
class JobOfferSkill(db.Model):
    __tablename__ = 'job_offer_skills'
    job_offer_id = db.Column(db.BigInteger, db.ForeignKey('job_offer.job_offer_id'), primary_key=True)
    skill_id = db.Column(db.BigInteger, db.ForeignKey('skills.skill_id'), primary_key=True)

# Applications Model
class Application(db.Model):
    __tablename__ = 'applications'
    application_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    applicant_id = db.Column(db.BigInteger, db.ForeignKey('applicants.applicant_id'), nullable=False)
    job_offer_id = db.Column(db.BigInteger, db.ForeignKey('job_offer.job_offer_id'), nullable=False)
