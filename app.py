from flask import Flask
from routes.views import index, trabajadores, planilla, asistencia, login

app = Flask(__name__)

app.add_url_rule("/", view_func=index)
app.add_url_rule("/trabajadores", view_func=trabajadores)
app.add_url_rule("/planilla", view_func=planilla)
app.add_url_rule("/asistencia", view_func=asistencia)
app.add_url_rule("/login", view_func=login)

if __name__ == "__main__":
    app.run(debug=True)



