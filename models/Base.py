from models.Ingrediente import Ingrediente

class Base(Ingrediente):
    def __init__(self, nombre: str, precio: float, calorias: int, unidades: float, es_vegetariano: bool, sabor: str):
        super().__init__(nombre, precio, calorias, unidades, es_vegetariano)
        self.__sabor = sabor

    def abastecer(self):
        '''Abastece cinco unidades del ingrediente base'''
        self.unidades += 5.0
        
    @property
    def sabor(self):
        return self.__sabor
    @sabor.setter
    def sabor(self, nuevo_sabor:str) -> str:
        if isinstance(nuevo_sabor, str) and nuevo_sabor != '':
            self.__sabor = nuevo_sabor
