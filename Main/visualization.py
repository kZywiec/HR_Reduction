import matplotlib.pyplot as plt

def plot_salary_distribution(job_offer, applicants, job_offer_id):
    plt.figure(figsize=(10, 6))
    plt.hist(
        [app['expected_salary'] for app in applicants],
        bins=15,
        alpha=0.7,
        label='Applicants'
    )
    plt.axvline(
        job_offer['salary'],
        color='r',
        linestyle='dashed',
        linewidth=2,
        label='Offered Salary'
    )
    plt.title('Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.legend()

    image_path = f'static/images/salary_distribution_{job_offer_id}.png'
    plt.savefig(image_path)
    plt.close()
    return image_path
