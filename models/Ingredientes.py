from config.db import db

class Ingredientes(db.Model):
    nombre = db.Column(db.Text(100), primary_key=True)
    precio = db.Column(db.Float(10), nullable=False)
    calorias = db.Column(db.Integer(10), nullable=False)
    unidades = db.Column(db.Float(10), nullable=False)
    es_vegetariano = db.Column(db.Bool, nullable=False)
    tipo_de_ingrediente = db.Column(db.Text(20), nullable=False)
    sabor = db.Column(db.Text(20), nullable=True)