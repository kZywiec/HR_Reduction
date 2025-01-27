from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# DB Server link
sql_server = 'LAPTOP-770L9VPM\\SQLEXPRESS' # Replace with yours 

# Inicjalizacja aplikacji Flask i konfiguracji bazy danych
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@'+ sql_server +'/HR_Reduction?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


with app.app_context():
    db.create_all()

__all__ = ['app', 'db']