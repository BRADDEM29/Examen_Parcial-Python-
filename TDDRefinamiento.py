import unittest

class Trabajador:
    def __init__(self, nombre, sueldo_basico, dias_falta, minutos_tardanza, horas_extras):
        self.nombre = nombre
        self.sueldo_basico = sueldo_basico
        self.dias_falta = dias_falta
        self.minutos_tardanza = minutos_tardanza
        self.horas_extras = horas_extras

    def calcular_sueldo(self):
        bonificaciones = self.calcular_bonificaciones()
        descuentos = self.calcular_descuentos()

        sueldo_neto = self.sueldo_basico + bonificaciones - descuentos
        return sueldo_neto

    def calcular_bonificaciones(self):
        pago_horas_extras = 1.50 * self.horas_extras * self.sueldo_basico / 30 / 8
        bonificacion_movilidad = 1000
        bonificacion_suplementaria = 0.03 * self.sueldo_basico
        bonificaciones = bonificacion_movilidad + bonificacion_suplementaria + pago_horas_extras
        return bonificaciones

    def calcular_descuentos(self):
        remuneracion_computable = self.sueldo_basico + self.calcular_bonificaciones()
        descuento_faltas = remuneracion_computable / 30 * self.dias_falta
        descuento_tardanzas = remuneracion_computable / 30 / 8 / 60 * self.minutos_tardanza
        descuentos = descuento_faltas + descuento_tardanzas
        return descuentos

    def imprimir_boleta_pago(self):
        sueldo_neto = self.calcular_sueldo()
        print("Nombre del trabajador:", self.nombre)
        print("Sueldo básico:", self.sueldo_basico)
        print("Días de falta:", self.dias_falta)
        print("Minutos de tardanza:", self.minutos_tardanza)
        print("Horas extras:", self.horas_extras)
        print("Sueldo neto a pagar:", sueldo_neto)


class TestTrabajador(unittest.TestCase):
    def test_calcular_bonificaciones(self):
        trabajador = Trabajador("Juan", 2000, 0, 0, 2)
        self.assertAlmostEqual(trabajador.calcular_bonificaciones(), 1085, places=2)

    def test_calcular_descuentos(self):
        trabajador = Trabajador("Juan", 2000, 0, 0, 2)
        self.assertAlmostEqual(trabajador.calcular_descuentos(), 0.0, places=2)

    def test_calcular_sueldo(self):
        sueldo_esperado = 3085
        trabajador = Trabajador("Juan", 2000, 0, 0, 2)
        self.assertAlmostEqual(trabajador.calcular_sueldo(),3085, sueldo_esperado)

if __name__ == "__main__":
    # unittest.main()  # Comentado para evitar que se ejecute automáticamente
    nombre_trabajador = input("Ingrese el nombre del trabajador: ")
    sueldo_basico = float(input("Ingrese el sueldo básico del trabajador: "))
    dias_falta = int(input("Ingrese los días de falta del trabajador: "))
    minutos_tardanza = int(input("Ingrese los minutos de tardanza del trabajador: "))
    horas_extras = int(input("Ingrese las horas extras trabajadas por el trabajador: "))
    trabajador = Trabajador(nombre_trabajador, sueldo_basico, dias_falta, minutos_tardanza, horas_extras)
    print("\n")
    trabajador.imprimir_boleta_pago()
    unittest.main()
