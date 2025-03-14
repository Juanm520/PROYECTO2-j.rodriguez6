from controllers.inicio_controller import inicio_blueprint

def register_routes(app):
    app.register_blueprint(inicio_blueprint)

    