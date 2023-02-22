from os import getcwd
from flask import Flask
from models.model import db
from routes.views import login, trabajadores, asistencia, desarrollo, planilla, admin, api
from routes.index import index

app = Flask(__name__)

app.secret_key = "Secret key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + getcwd() + '\databases\database.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.add_url_rule("/login", view_func=login)
app.add_url_rule("/", methods=["GET", "POST"], view_func=index)
app.add_url_rule("/trabajadores", view_func=trabajadores)
app.add_url_rule("/asistencia", view_func=asistencia)
app.add_url_rule("/desarrollo", view_func=desarrollo)
app.add_url_rule("/planilla", view_func=planilla)
app.add_url_rule("/admin", methods=["GET", "POST"], view_func=admin)
app.add_url_rule("/api", methods=["POST"], view_func=api)

if __name__ == "__main__":      
    app.run(debug=True)  #, host="0.0.0.0", port=5000)



