from flask import render_template
import os

# Replace these with actual modules where the functions are implemented
from Config.Models import get_job_offer_details, get_required_skills, get_matching_applicants
from Processing.visualization import plot_salary_distribution


def generate_report(job_offer_id, experience_margin=2, salary_margin=5000, skill_margin=2):
    # Fetch job offer details
    job_offer = get_job_offer_details(job_offer_id)[0]
    required_skills = get_required_skills(job_offer_id)
    applicants = get_matching_applicants(job_offer_id)

    # Filter applicants based on the provided margins
    filtered_applicants = []
    for app in applicants:
        if (
            abs(app['experience'] - job_offer['required_experience']) <= experience_margin and
            abs(app['expected_salary'] - job_offer['salary']) <= salary_margin and
            len(set(app['skill_name'].split(',')).intersection(required_skills)) >= skill_margin
        ):
            filtered_applicants.append(app)

    # Generate visualizations
    salary_chart = plot_salary_distribution(job_offer, filtered_applicants, job_offer_id)

    # Render and save the report
    report_html = render_template(
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
        salary_chart=salary_chart
    )

    # Ensure the reports directory exists
    reports_dir = os.path.join('static', 'reports')
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    # Save the report
    report_path = os.path.join(reports_dir, f'report_{job_offer_id}.html')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_html)

    return report_path
