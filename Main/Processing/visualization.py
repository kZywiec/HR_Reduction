import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
import base64
import seaborn as sns
import pandas as pd


def plot_salary_distribution(job_offer, filtered_applicants, job_offer_id):
    salaries = [app['expected_salary'] for app in filtered_applicants]
    names = [app['applicant_name'] for app in filtered_applicants]

    plt.figure(figsize=(10, 6))
    plt.bar(names, salaries, color='blue', alpha=0.7, label='Applicants')
    plt.axhline(y=job_offer['salary'], color='red', linestyle='--', label='Job Offer Salary')
    plt.xlabel('Applicants')
    plt.ylabel('Salary ($)')
    plt.title('Salary Distribution')
    plt.xticks(rotation=45, ha='right')  # Rotate names for better visibility
    plt.legend()

    img_io = io.BytesIO()
    plt.savefig(img_io, format='png', bbox_inches='tight')
    img_io.seek(0)
    plt.close()

    return f"data:image/png;base64,{base64.b64encode(img_io.read()).decode('utf-8')}"


def plot_skill_match_distribution(filtered_applicants, required_skills):
    skill_matches = [
        len(set(app['skill_name'].split(',')).intersection(required_skills))
        for app in filtered_applicants
    ]
    names = [app['applicant_name'] for app in filtered_applicants]

    plt.figure(figsize=(10, 6))
    plt.bar(names, skill_matches, color='green', alpha=0.7)
    plt.xlabel('Applicants')
    plt.ylabel('Number of Matching Skills')
    plt.title('Skill Match Distribution')
    plt.xticks(rotation=45, ha='right')

    img_io = io.BytesIO()
    plt.savefig(img_io, format='png', bbox_inches='tight')
    img_io.seek(0)
    plt.close()

    return f"data:image/png;base64,{base64.b64encode(img_io.read()).decode('utf-8')}"


def plot_experience_distribution(filtered_applicants):
    experiences = [app['experience'] for app in filtered_applicants]
    names = [app['applicant_name'] for app in filtered_applicants]

    plt.figure(figsize=(10, 6))
    plt.bar(names, experiences, color='orange', alpha=0.7)
    plt.xlabel('Applicants')
    plt.ylabel('Years of Experience')
    plt.title('Experience Distribution')
    plt.xticks(rotation=45, ha='right')

    img_io = io.BytesIO()
    plt.savefig(img_io, format='png', bbox_inches='tight')
    img_io.seek(0)
    plt.close()

    return f"data:image/png;base64,{base64.b64encode(img_io.read()).decode('utf-8')}"


def plot_experience_vs_salary(filtered_applicants):
    experiences = [app['experience'] for app in filtered_applicants]
    salaries = [app['expected_salary'] for app in filtered_applicants]
    names = [app['applicant_name'] for app in filtered_applicants]

    plt.figure(figsize=(10, 6))
    plt.scatter(experiences, salaries, color='blue', s=100, alpha=0.7)
    for i, name in enumerate(names):
        plt.text(experiences[i], salaries[i], name, fontsize=9, ha='right', va='bottom')
    plt.xlabel('Experience (Years)')
    plt.ylabel('Requested Salary ($)')
    plt.title('Experience vs. Salary')

    img_io = io.BytesIO()
    plt.savefig(img_io, format='png', bbox_inches='tight')
    img_io.seek(0)
    plt.close()

    return f"data:image/png;base64,{base64.b64encode(img_io.read()).decode('utf-8')}"


def plot_skill_coverage(filtered_applicants, required_skills):
    skill_counts = {skill: 0 for skill in required_skills}
    for app in filtered_applicants:
        applicant_skills = set(app['skill_name'].split(','))
        for skill in required_skills:
            if skill in applicant_skills:
                skill_counts[skill] += 1

    plt.figure(figsize=(10, 6))
    plt.bar(skill_counts.keys(), skill_counts.values(), color='green', alpha=0.7)
    plt.xlabel('Skills')
    plt.ylabel('Number of Applicants with Skill')
    plt.title('Skill Coverage')
    plt.xticks(rotation=45, ha='right')

    img_io = io.BytesIO()
    plt.savefig(img_io, format='png', bbox_inches='tight')
    img_io.seek(0)
    plt.close()

    return f"data:image/png;base64,{base64.b64encode(img_io.read()).decode('utf-8')}"


def plot_skill_match_heatmap(filtered_applicants, required_skills):
    data = []
    for app in filtered_applicants:
        applicant_skills = set(app['skill_name'].split(','))
        data.append([1 if skill in applicant_skills else 0 for skill in required_skills])

    df = pd.DataFrame(data, columns=required_skills, index=[app['applicant_name'] for app in filtered_applicants])
    if df.empty:
        # Generate a blank plot with a warning if DataFrame is unexpectedly empty
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(0.5, 0.5, 'No valid skill match data', 
                horizontalalignment='center', verticalalignment='center', 
                fontsize=14, color='red', transform=ax.transAxes)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_frame_on(False)

        img_io = io.BytesIO()
        fig.savefig(img_io, format='png', bbox_inches='tight')
        img_io.seek(0)
        plt.close(fig)

        return f"data:image/png;base64,{base64.b64encode(img_io.read()).decode('utf-8')}"
    plt.figure(figsize=(10, len(filtered_applicants) * 0.5))
    sns.heatmap(df, annot=True, cbar=False, cmap="YlGnBu", linewidths=0.5)
    plt.xlabel('Required Skills')
    plt.ylabel('Applicants')
    plt.title('Skill Match Heatmap')

    img_io = io.BytesIO()
    plt.savefig(img_io, format='png', bbox_inches='tight')
    img_io.seek(0)
    plt.close()

    return f"data:image/png;base64,{base64.b64encode(img_io.read()).decode('utf-8')}"
