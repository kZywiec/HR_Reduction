from Config.DataBase import app, db
from Config.Models import JobOffer
from sqlalchemy import or_, distinct

def search_job_offers(filters):
    with app.app_context():  # Użycie kontekstu aplikacji
        query = db.session.query(
            JobOffer.job_offer_id,
            JobOffer.job_title,
            JobOffer.role_category,
            JobOffer.location,
            JobOffer.functional_area,
            JobOffer.industry,
            JobOffer.salary,
            JobOffer.required_experience
        ).distinct()

        # Dodaj warunki tylko dla wypełnionych filtrów
        conditions = []
        for column, value in filters.items():
            if value:
                conditions.append(getattr(JobOffer, column).ilike(f"%{value}%"))

        if conditions:
            query = query.filter(or_(*conditions))

        results = query.all()
        return [
            {
                "job_offer_id": result.job_offer_id,
                "job_title": result.job_title,
                "role_category": result.role_category,
                "location": result.location,
                "functional_area": result.functional_area,
                "industry": result.industry,
                "salary": result.salary,
                "required_experience": result.required_experience
            }
            for result in results
        ]

