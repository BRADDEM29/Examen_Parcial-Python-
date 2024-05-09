def ingresar_datos():
    nombre_trabajador = input("Ingrese el nombre del trabajador: ")
    sueldo_basico = float(input("Ingrese el sueldo básico del trabajador: "))
    dias_falta = int(input("Ingrese los días de falta del trabajador: "))
    minutos_tardanza = int(input("Ingrese los minutos de tardanza del trabajador: "))
    horas_extra = float(input("Ingrese las horas extras trabajadas: "))
    return nombre_trabajador, sueldo_basico, dias_falta, minutos_tardanza, horas_extra


def calcular_bonificaciones(sueldo_basico, horas_extra):
    # Cálculo del pago por horas extras
    pago_horas_extras = 1.50 * horas_extra * sueldo_basico / 30 / 8
    
    # Bonificaciones
    bonificacion_movilidad = 1000
    bonificacion_suplementaria = 0.03 * sueldo_basico
    
    # Bonificaciones totales
    bonificaciones = bonificacion_movilidad + bonificacion_suplementaria + pago_horas_extras
    
    return bonificaciones


def calcular_descuentos(sueldo_basico, bonificaciones, dias_falta, minutos_tardanza):
    # Remuneración mínima
    remuneracion_minima = sueldo_basico + bonificaciones
    
    # Descuento por faltas
    descuento_faltas = remuneracion_minima / 30 * dias_falta
    
    # Descuento por tardanzas
    descuento_tardanzas = remuneracion_minima / 30 / 8 / 60 * minutos_tardanza
    
    # Total de descuentos
    total_descuentos = descuento_faltas + descuento_tardanzas
    
    return total_descuentos


def calcular_sueldo_neto(sueldo_basico, bonificaciones, descuentos):
    sueldo_neto = sueldo_basico + bonificaciones - descuentos
    return sueldo_neto


def imprimir_boleta(nombre_trabajador, sueldo_neto, bonificaciones, descuentos):
    print("------- Boleta de Pago -------")
    print(f"Nombre del trabajador: {nombre_trabajador}")
    print(f"Sueldo a pagar: ${sueldo_neto:.2f}")
    print(f"Bonificación total: ${bonificaciones:.2f}")
    print(f"Total de descuentos: ${descuentos:.2f}")
    print("-------------------------------")


if __name__ == "__main__":
    # Ingreso de datos
    nombre_trabajador, sueldo_basico, dias_falta, minutos_tardanza, horas_extra = ingresar_datos()
    
    # Cálculo del sueldo a pagar
    bonificaciones = calcular_bonificaciones(sueldo_basico, horas_extra)
    descuentos = calcular_descuentos(sueldo_basico, bonificaciones, dias_falta, minutos_tardanza)
    sueldo_neto = calcular_sueldo_neto(sueldo_basico, bonificaciones, descuentos)
    
    # Impresión de la boleta de pago
    imprimir_boleta(nombre_trabajador, sueldo_neto, bonificaciones, descuentos)
