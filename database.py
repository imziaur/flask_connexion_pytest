from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db_url = 'postgresql+psycopg2://postgres:postgres_pass@localhost/connexion_pytest'