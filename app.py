from flask import Flask
from config.config import Config
from config.db import db
from config.routes import register_routes
from crear_filas_iniciales import crear_filas

app = Flask(__name__, template_folder='views')
app.config.from_object(Config)
db.init_app(app)

register_routes(app)

with app.app_context():
    db.create_all()
    crear_filas(db)

if __name__ == '__main__':
    app.run(debug=True)
