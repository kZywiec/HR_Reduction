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

