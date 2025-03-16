from flask import Blueprint, render_template
from models.Heladeria import Heladeria
from models.Productos_db import Producto
from models.Ingredientes_db import Ingrediente
from models.Base import Base
from models.Complemento import Complemento
from models.Copa import Copa
from models.Malteada import Malteada

heladeria_blueprint = Blueprint('heladeria', __name__, url_prefix = '/heladeria')

@heladeria_blueprint.route('/')
def heladeria_controller():
    '''Controlador de la Heladeria'''

    #Llama los Ingredientes en la base de datos.
    ingredientes_query = Ingrediente.query.all()
    ingredientes_disponibles = []
    for ingrediente in ingredientes_query:
            #Itera los ingredientes para las agregar a las instancias de Ingredientes.'''
            if ingrediente.tipo_de_ingrediente == 'Base':
                ingredientes_disponibles.append(Base(ingrediente.nombre, ingrediente.precio, ingrediente.calorias, ingrediente.unidades, ingrediente.es_vegetariano, ingrediente.sabor))
            else:
                ingredientes_disponibles.append(Complemento(ingrediente.nombre, ingrediente.precio, ingrediente.calorias, ingrediente.unidades, ingrediente.es_vegetariano))
    #Llama los productos en la base de datos.
    productos_query = Producto.query.all()
    #Crea lista de las instancias productos
    productos_disponibles = []

    for producto in productos_query:
        #Itera los productos para construir sus instancias.
        ingredientes_clase_producto = []
        ingredientes_producto = [producto.ingrediente1, producto.ingrediente2, producto.ingrediente3]
        #Itera los ingredientes para agregarlos al producto.
        for ingrediente_producto in ingredientes_producto:
            for ingrediente in ingredientes_disponibles:
                if ingrediente.nombre == ingrediente_producto:
                    ingredientes_clase_producto.append(ingrediente)
            
        #Crea las instancias de los prodcutos.
        if producto.tipo_de_producto == 'Copa':
            productos_disponibles.append(Copa(producto.nombre, producto.precio_publico, ingredientes_clase_producto, producto.tipo_vaso))
        else:
            productos_disponibles.append(Malteada(producto.nombre, producto.precio_publico, ingredientes_clase_producto, producto.volumen))

    #Iniciando la Heladeria
    heladeria = Heladeria('Sammy el Heladero', productos_disponibles)

    #Ventas de comprobacion y para agregar saldo a las ventas diarias.
    a_vender = [productos_disponibles[0], productos_disponibles[1], productos_disponibles[1], productos_disponibles[3]]
    vendido = []
    for producto in a_vender:
        try:
            vendido.append((producto.nombre, producto.precio_publico, heladeria.vender(producto.nombre)))
        except ValueError as error:
            vendido.append((producto.nombre, 0, error))

    #A presentar en el frontend:
    salida = {
        'rentable': heladeria.producto_mas_rentable(),
        'ventas': heladeria.ventas_del_dia,
        'productos': heladeria.productos,
        'vendido': vendido
    }
    
    return render_template('heladeria.html', salida = salida)
