from flask import Flask
from Main.report_generator import generate_report

# Initialize Flask app
app = Flask(__name__)

@app.route('/generate_report/<int:job_offer_id>')
def generate_report_route(job_offer_id):
    report_path = generate_report(job_offer_id)
    return f"Report generated at: {report_path}"

if __name__ == '__main__':
    app.run(debug=True)
