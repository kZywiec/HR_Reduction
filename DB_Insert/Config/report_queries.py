from DB_Insert.Config.DataBase import db

def get_job_offer_details(job_offer_id):
    query = f"""
    SELECT * FROM job_offer
    WHERE job_offer_id = {job_offer_id};
    """
    result = db.session.execute(query).fetchall()
    return [dict(row) for row in result]

def get_required_skills(job_offer_id):
    query = f"""
    SELECT s.skill_name
    FROM job_offer_skills jos
    JOIN skills s ON jos.skill_id = s.skill_id
    WHERE jos.job_offer_id = {job_offer_id};
    """
    result = db.session.execute(query).fetchall()
    return [row['skill_name'] for row in result]

def get_matching_applicants(job_offer_id):
    query = f"""
    SELECT a.applicant_name, a.experience, a.expected_salary, s.skill_name
    FROM applications ap
    JOIN applicants a ON ap.applicant_id = a.applicant_id
    JOIN applicant_skills aks ON a.applicant_id = aks.applicant_id
    JOIN skills s ON aks.skill_id = s.skill_id
    WHERE ap.job_offer_id = {job_offer_id};
    """
    result = db.session.execute(query).fetchall()
    return [dict(row) for row in result]
