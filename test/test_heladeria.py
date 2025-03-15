import unittest
from models.Base import Base
from models.Complemento import Complemento
from models.Copa import Copa
from models.Malteada import Malteada
from models.Heladeria import Heladeria

class TestEsSano(unittest.TestCase):
    '''Test a las instancias Ingredientes'''
    def test_ingrediente_es_sano_menos_de_cien_calorias(self):
        ingrediente = Base('Helado de Fresa', 1200, 26, 1, False, 'Fresa')
        self.assertEqual(ingrediente.es_sano(), not ingrediente.es_vegetariano and ingrediente.calorias < 100)

    def test_ingrediente_es_sano_mas_de_cien_calorias_vegetariano(self):
        ingrediente = Base('Mix Frutas Congeladas', 1450, 120, 10, True, 'Banano, Kiwi y Fresa')
        self.assertEqual(ingrediente.es_sano(), ingrediente.es_vegetariano and ingrediente.calorias > 100)

    def test_ingrediente_no_es_sano_mas_de_cien_calorias(self):
        ingrediente = Base('Helado de Chocolate', 1900, 120, 10, False, 'Chocolate')
        self.assertFalse(ingrediente.es_sano(), ingrediente.es_vegetariano and ingrediente.calorias > 100)

class TestAbastecer(unittest.TestCase):
    def test_abastece_correctamente_un_ingrediente_base(self):
        ingrediente = Base('Helado de Fresa', 1200, 26, 0, False, 'Fresa')
        ingrediente.abastecer()
        self.assertEqual(ingrediente.unidades, 5)

    def test_abastece_correctamente_un_ingrediente_complemento(self):
        ingrediente = Complemento('Chispas de chocolate', 500, 20, 0, False)
        ingrediente.abastecer()
        self.assertEqual(ingrediente.unidades, 10)

class TestRenovarInventario(unittest.TestCase):
    def test_renueva_correctamente_un_ingrediente_complemento(self):
        ingrediente = Complemento('Chispas de chocolate', 500, 20, 5, False)
        ingrediente.renovar_inventario()
        self.assertEqual(ingrediente.unidades, 0)

class TestProductos(unittest.TestCase):
    def test_calcular_calorias_en_una_copa(self):
        helado_fresa = Base('Helado de Fresa', 1200, 26, 1, False, 'Fresa')
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        ingredientes_copa_junior = [helado_fresa, chispas_chocolate, mani]
        copa_junior = Copa('Copa Junior', 12000, ingredientes_copa_junior, "mediano")
        calorias_totales = 0
        for ingrediente in copa_junior.ingredientes:
            calorias_totales += ingrediente.calorias
        self.assertEqual(copa_junior.calcular_calorias(), round(calorias_totales * 0.95, 2))

    def test_calcular_calorias_en_una_malteada(self):
        helado_mandarina = Base('Helado de Mandarina', 1200, 40, 0, False, 'Mandarina')
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        ingredientes_malteada_mandarina = [helado_mandarina, mani, chispas_chocolate]
        malteada_mandarina = Malteada('Malteada de Mandarina', 18000, ingredientes_malteada_mandarina, 13)
        calorias_totales = 200
        for ingrediente in malteada_mandarina.ingredientes:
            calorias_totales += ingrediente.calorias
        self.assertEqual(malteada_mandarina.calcular_calorias(), calorias_totales)

    def test_calcular_costos_en_una_copa(self):
        helado_fresa = Base('Helado de Fresa', 1200, 26, 1, False, 'Fresa')
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        ingredientes_copa_junior = [helado_fresa, chispas_chocolate, mani]
        copa_junior = Copa('Copa Junior', 12000, ingredientes_copa_junior, "mediano")
        costo = 0
        for ingrediente in copa_junior.ingredientes:
            costo += ingrediente.precio
        self.assertEqual(copa_junior.calcular_costo(), costo)

    def test_calcular_costos_en_una_malteada(self):
        helado_mandarina = Base('Helado de Mandarina', 1200, 40, 0, False, 'Mandarina')
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        ingredientes_malteada_mandarina = [helado_mandarina, mani, chispas_chocolate]
        malteada_mandarina = Malteada('Malteada de Mandarina', 18000, ingredientes_malteada_mandarina, 13)
        costo = 500
        for ingrediente in malteada_mandarina.ingredientes:
            costo += ingrediente.precio
        self.assertEqual(malteada_mandarina.calcular_costo(), costo)

    def test_calcular_rentabilidad_en_una_copa(self):
        helado_fresa = Base('Helado de Fresa', 1200, 26, 1, False, 'Fresa')
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        ingredientes_copa_junior = [helado_fresa, chispas_chocolate, mani]
        copa_junior = Copa('Copa Junior', 12000, ingredientes_copa_junior, "mediano")
        rentabilidad = copa_junior.precio_publico - copa_junior.calcular_costo()
        self.assertEqual(copa_junior.calcular_rentabilidad(), rentabilidad)

    def test_calcular_rentabilidad_en_una_malteada(self):
        helado_mandarina = Base('Helado de Mandarina', 1200, 40, 0, False, 'Mandarina')
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        ingredientes_malteada_mandarina = [helado_mandarina, mani, chispas_chocolate]
        malteada_mandarina = Malteada('Malteada de Mandarina', 18000, ingredientes_malteada_mandarina, 13)
        rentabilidad = malteada_mandarina.precio_publico - malteada_mandarina.calcular_costo()
        self.assertEqual(malteada_mandarina.calcular_rentabilidad(), rentabilidad)

class TestHeladeria(unittest.TestCase):
    def test_producto_mas_rentable_en_la_heladeria(self):
        helado_mandarina = Base('Helado de Mandarina', 1200, 40, 0, False, 'Mandarina')
        mani = Complemento('Mani', 900, 35, 5, True)
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        helado_fresa = Base('Helado de Fresa', 1200, 26, 1, False, 'Fresa')
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        ingredientes_malteada_mandarina = [helado_mandarina, mani, chispas_chocolate]
        ingredientes_copa_junior = [helado_fresa, chispas_chocolate, mani]
        malteada_mandarina = Malteada('Malteada de Mandarina', 18000, ingredientes_malteada_mandarina, 13)
        copa_junior = Copa('Copa Junior', 12000, ingredientes_copa_junior, "mediano")
        rentabilidad_malteada = 15400
        rentabilidad_copa = 9400
        heladeria=Heladeria('Helados', [copa_junior, malteada_mandarina])
        self.assertEqual(heladeria.producto_mas_rentable(), 'Malteada de Mandarina')

    
if __name__ == "__main__":
    unittest.main()
