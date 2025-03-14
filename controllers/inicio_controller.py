from flask import Blueprint, render_template

inicio_blueprint = Blueprint('inicio', __name__, url_prefix = '/')

@inicio_blueprint.route('/')
def inicio_controller():
    return render_template('index.html')
