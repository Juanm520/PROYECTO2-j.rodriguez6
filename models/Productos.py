from config.db import db

class Producto(db.Model):
    nombre = db.Column(db.Text(100), primary_key=True)
    precio_publico = db.Column(db.Float(13), nullable=False)
    ingredientes = db.Column(db.Array(3), nullable=False)
    tipo_de_producto = db.Column(db.Text(50), nullable=False)
    tipo_de_vaso = db.Column(db.Text(20), nullable=True)
    volumen = db.Column(db.Integer(20), nullable=True)