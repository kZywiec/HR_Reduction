"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify
from Main import app
from Main.Utils.search_job_offers import search_job_offers

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/search_job_offers', methods=['POST'])
def search_job_offers_endpoint():
    """
    Endpoint do wyszukiwania ofert pracy.
    """
    filters = request.json  # Odbierz dane JSON z formularza
    results = search_job_offers(filters)  # Wywołaj funkcję wyszukiwania
    return jsonify(results)  # Zwróć wyniki jako JSON
