from models.Ingrediente import Ingrediente

class Complemento(Ingrediente):
    def __init__(self, nombre: str, precio: float, calorias: int, unidades: float, es_vegetariano: bool):
        super().__init__(nombre, precio, calorias, unidades, es_vegetariano)
       
    def abastecer(self):
        '''Abastece cinco unidades del ingrediente base.'''
        self.unidades += 10.0

    def renovar_inventario(self):
        '''Devuelve a cero las unidades del ingrediente.'''
        self.unidades = 0.0
