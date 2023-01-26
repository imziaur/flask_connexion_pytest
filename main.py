
from flask import jsonify
import connexion
from database import db, db_url
app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('swagger.yml')
app=app.app
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)