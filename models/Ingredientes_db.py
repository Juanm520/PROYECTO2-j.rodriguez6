from config.db import db

class Ingrediente(db.Model):
    '''Modelo de Ingrediente en la base de datos.'''
    nombre = db.Column(db.Text, primary_key=True)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    unidades = db.Column(db.Float, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)
    tipo_de_ingrediente = db.Column(db.Text, nullable=False)
    sabor = db.Column(db.Text, nullable=True)

    @staticmethod
    def commit():
        '''Evita la importacion de db y dispone el metodo en donde se requiera afectar la tabla.'''
        db.session.commit()
