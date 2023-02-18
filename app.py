from flask import Flask
from routes.views import login, index, trabajadores, asistencia, desarrollo, planilla, admin

app = Flask(__name__)

app.add_url_rule("/login", view_func=login)
app.add_url_rule("/", view_func=index)
app.add_url_rule("/trabajadores", view_func=trabajadores)
app.add_url_rule("/asistencia", view_func=asistencia)
app.add_url_rule("/desarrollo", view_func=desarrollo)
app.add_url_rule("/planilla", view_func=planilla)

app.add_url_rule("/admin", methods=["GET", "POST"], view_func=admin)

if __name__ == "__main__":
    app.run(debug=True)



