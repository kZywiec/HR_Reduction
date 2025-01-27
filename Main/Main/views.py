"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify
from Main import app
from Main.Utils.search_job_offers import search_job_offers
from Processing.report_generator import generate_report
from flask import Flask, request, render_template
from Processing.report_generator import get_job_offer_details, get_required_skills, get_matching_applicants
from Processing.visualization import (
    plot_salary_distribution,
    plot_skill_match_distribution,
    plot_experience_distribution,
    plot_experience_vs_salary,
    plot_skill_coverage,
    plot_skill_match_heatmap
)

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



@app.route('/generate_report')
def generate_report_route():
    # Fetch query parameters from the request
    job_offer_id = int(request.args.get('job_offer_id'))
    experience_margin = int(request.args.get('experience_margin'))
    salary_margin = int(request.args.get('salary_margin'))
    skill_margin = int(request.args.get('skill_margin'))

    # Fetch job offer details, required skills, and applicants
    job_offer = get_job_offer_details(job_offer_id)[0]
    required_skills = get_required_skills(job_offer_id)
    applicants = get_matching_applicants(job_offer_id)

    # Filter applicants based on the provided margins
    filtered_applicants = [
        app for app in applicants
        if (
            abs(app['experience'] - job_offer['required_experience']) <= experience_margin and
            abs(app['expected_salary'] - job_offer['salary']) <= salary_margin and
            len(set(app['skill_name'].split(',')).intersection(required_skills)) >= skill_margin
        )
    ]

   # Generate plots
    salary_chart = plot_salary_distribution(job_offer, filtered_applicants, job_offer_id)
    skill_match_chart = plot_skill_match_distribution(filtered_applicants, required_skills)
    experience_chart = plot_experience_distribution(filtered_applicants)
    experience_vs_salary_chart = plot_experience_vs_salary(filtered_applicants)
    skill_coverage_chart = plot_skill_coverage(filtered_applicants, required_skills)
    skill_heatmap_chart = plot_skill_match_heatmap(filtered_applicants, required_skills)

    # Render report
    return render_template(
        'report_template.html',
        job_title=job_offer['job_title'],
        location=job_offer['location'],
        salary=job_offer['salary'],
        required_skills=required_skills,
        candidates=[
            {
                'name': app['applicant_name'],
                'experience': app['experience'],
                'req_salary': app['expected_salary'],
                'skills': app['skill_name'],
            }
            for app in filtered_applicants
        ],
        salary_chart=salary_chart,
        skill_match_chart=skill_match_chart,
        experience_chart=experience_chart,
        experience_vs_salary_chart=experience_vs_salary_chart,
        skill_coverage_chart=skill_coverage_chart,
        skill_heatmap_chart=skill_heatmap_chart
    )

