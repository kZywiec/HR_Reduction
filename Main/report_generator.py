from flask import render_template
from DB_Insert.Config.report_queries import get_job_offer_details, get_required_skills, get_matching_applicants
from Main.visualization import plot_salary_distribution

def generate_report(job_offer_id):
    # Fetch job offer details
    job_offer = get_job_offer_details(job_offer_id)[0]
    required_skills = get_required_skills(job_offer_id)
    applicants = get_matching_applicants(job_offer_id)

    # Generate salary chart
    salary_chart = plot_salary_distribution(job_offer, applicants, job_offer_id)

    # Render HTML using Flask's render_template
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
            for app in applicants
        ],
        salary_chart=salary_chart
    )

    # Save the report to an HTML file
    report_path = f'output/report_{job_offer_id}.html'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_html)

    return report_path
