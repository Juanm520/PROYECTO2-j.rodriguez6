from controllers.inicio_controller import inicio_blueprint
from controllers.heladeria_controller import heladeria_blueprint

def register_routes(app):
    app.register_blueprint(inicio_blueprint)
    app.register_blueprint(heladeria_blueprint)
    