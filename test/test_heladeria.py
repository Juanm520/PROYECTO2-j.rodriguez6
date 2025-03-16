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
        #implementacion del Test
        self.assertEqual(ingrediente.es_sano(), not ingrediente.es_vegetariano and ingrediente.calorias < 100)

    def test_ingrediente_es_sano_mas_de_cien_calorias_vegetariano(self):
        ingrediente = Base('Mix Frutas Congeladas', 1450, 120, 10, True, 'Banano, Kiwi y Fresa')
        #implementacion del Test
        self.assertEqual(ingrediente.es_sano(), ingrediente.es_vegetariano and ingrediente.calorias > 100)

    def test_ingrediente_no_es_sano_mas_de_cien_calorias(self):
        ingrediente = Base('Helado de Chocolate', 1900, 120, 10, False, 'Chocolate')
        #implementacion del Test
        self.assertFalse(ingrediente.es_sano(), ingrediente.es_vegetariano and ingrediente.calorias > 100)

class TestAbastecer(unittest.TestCase):
    def test_abastece_correctamente_un_ingrediente_base(self):
        ingrediente = Base('Helado de Fresa', 1200, 26, 0, False, 'Fresa')
        #implementacion del Test
        ingrediente.abastecer()
        self.assertEqual(ingrediente.unidades, 5)

    def test_abastece_correctamente_un_ingrediente_complemento(self):
        ingrediente = Complemento('Chispas de chocolate', 500, 20, 0, False)
        #implementacion del Test
        ingrediente.abastecer()
        self.assertEqual(ingrediente.unidades, 10)

class TestRenovarInventario(unittest.TestCase):
    def test_renueva_correctamente_un_ingrediente_complemento(self):
        ingrediente = Complemento('Chispas de chocolate', 500, 20, 5, False)
        #implementacion del Test
        ingrediente.renovar_inventario()
        self.assertEqual(ingrediente.unidades, 0)

class TestProductos(unittest.TestCase):
    def test_calcular_calorias_en_una_copa(self):
        helado_fresa = Base('Helado de Fresa', 1200, 26, 1, False, 'Fresa')
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        ingredientes_copa_junior = [helado_fresa, chispas_chocolate, mani]
        copa_junior = Copa('Copa Junior', 12000, ingredientes_copa_junior, "mediano")
        #implementacion del Test
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
        #implementacion del Test
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
        #implementacion del Test
        costo = 0
        for ingrediente in copa_junior.ingredientes:
            costo += ingrediente.precio
        self.assertEqual(copa_junior.calcular_costo(), costo)
        #implementacion del Test
    def test_calcular_costos_en_una_malteada(self):
        helado_mandarina = Base('Helado de Mandarina', 1200, 40, 0, False, 'Mandarina')
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        ingredientes_malteada_mandarina = [helado_mandarina, mani, chispas_chocolate]
        malteada_mandarina = Malteada('Malteada de Mandarina', 18000, ingredientes_malteada_mandarina, 13)
        #implementacion del Test
        costo = 500
        for ingrediente in malteada_mandarina.ingredientes:
            costo += ingrediente.precio
        self.assertEqual(malteada_mandarina.calcular_costo(), costo)
        #implementacion del Test
    def test_calcular_rentabilidad_en_una_copa(self):
        helado_fresa = Base('Helado de Fresa', 1200, 26, 1, False, 'Fresa')
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        ingredientes_copa_junior = [helado_fresa, chispas_chocolate, mani]
        copa_junior = Copa('Copa Junior', 12000, ingredientes_copa_junior, "mediano")
        #implementacion del Test
        rentabilidad = copa_junior.precio_publico - copa_junior.calcular_costo()
        self.assertEqual(copa_junior.calcular_rentabilidad(), rentabilidad)

    def test_calcular_rentabilidad_en_una_malteada(self):
        helado_mandarina = Base('Helado de Mandarina', 1200, 40, 0, False, 'Mandarina')
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        ingredientes_malteada_mandarina = [helado_mandarina, mani, chispas_chocolate]
        malteada_mandarina = Malteada('Malteada de Mandarina', 18000, ingredientes_malteada_mandarina, 13)
        #implementacion del Test
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
        #implementacion del Test
        heladeria=Heladeria('Helados', [copa_junior, malteada_mandarina])
        rentabilidad_copa = heladeria.productos[0].calcular_rentabilidad()
        rentabilidad_malteada = heladeria.productos[1].calcular_rentabilidad()
        self.assertEqual(heladeria.producto_mas_rentable(), 'Malteada de Mandarina' if rentabilidad_malteada > rentabilidad_copa else 'Copa Junior')

    def test_venta_exitosa(self):
        helado_mandarina = Base('Helado de Mandarina', 1200, 40, 1, False, 'Mandarina')
        mani = Complemento('Mani', 900, 35, 5, True)
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        ingredientes_malteada_mandarina = [helado_mandarina, mani, chispas_chocolate]
        malteada_mandarina = Malteada('Malteada de Mandarina', 18000, ingredientes_malteada_mandarina, 13)
        heladeria=Heladeria('Helados', [malteada_mandarina])
        #implementacion del Test
        self.assertEqual(heladeria.vender('Malteada de Mandarina'), '¡Vendido!')

    def test_venta_fallida_por_no_existe_producto(self):
        helado_mandarina = Base('Helado de Mandarina', 1200, 40, 0, False, 'Mandarina')
        mani = Complemento('Mani', 900, 35, 5, True)
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        ingredientes_malteada_mandarina = [helado_mandarina, mani, chispas_chocolate]
        malteada_mandarina = Malteada('Malteada de Mandarina', 18000, ingredientes_malteada_mandarina, 13)
        heladeria=Heladeria('Helados', [malteada_mandarina])
        #implementacion del Test
        with self.assertRaises(ValueError):
            heladeria.vender('Copa Chocolate')
        
    def test_venta_fallida_por_ingrediente(self):
        helado_mandarina = Base('Helado de Mandarina', 1200, 40, 0, False, 'Mandarina')
        mani = Complemento('Mani', 900, 35, 5, True)
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        ingredientes_malteada_mandarina = [helado_mandarina, mani, chispas_chocolate]
        malteada_mandarina = Malteada('Malteada de Mandarina', 18000, ingredientes_malteada_mandarina, 13)
        heladeria=Heladeria('Helados', [malteada_mandarina])
        #implementacion del Test
        with self.assertRaises(ValueError):
            heladeria.vender('Malteada de Mandarina')
 
if __name__ == "__main__":
    unittest.main()
