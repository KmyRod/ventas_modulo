# Módulo inicial de procesamiento de ventas

DESCUENTO_PORCENTAJE = 0.9
UMBRAL_DESCUENTO_ESTANDAR = 1000
UMBRAL_DESCUENTO_VIP = 500


def aplica_descuento(transaccion):
    monto = transaccion['monto']
    cliente_tipo = transaccion['cliente_tipo']
    if monto > UMBRAL_DESCUENTO_ESTANDAR:
        return monto * DESCUENTO_PORCENTAJE
    if cliente_tipo == 'VIP' and monto > UMBRAL_DESCUENTO_VIP:
        return monto * DESCUENTO_PORCENTAJE
    return monto


def registrar_log(nombre_cliente):
    print("Procesando registro de: " + nombre_cliente)


def formatear_resultado_venta(transaccion):
    monto_final = aplica_descuento(transaccion)
    return "Cliente: " + transaccion['nombre'] + " - Total: " + str(monto_final)


def formatear_resultado_devolucion(transaccion):
    monto_retorno = transaccion['monto'] * -1
    return "Cliente: " + transaccion['nombre'] + " - Retorno: " + str(monto_retorno)


def procesar_transacciones(lista_transacciones):

    resultados = []

    for transaccion in lista_transacciones:

        if transaccion['tipo'] == 'venta' and transaccion['monto'] > 0 and transaccion['estado'] == 'completado':
            resultado = formatear_resultado_venta(transaccion)
            resultados.append(resultado)
            registrar_log(transaccion['nombre'])

        elif transaccion['tipo'] == 'devolucion' and transaccion['monto'] > 0:
            resultado = formatear_resultado_devolucion(transaccion)
            resultados.append(resultado)
            registrar_log(transaccion['nombre'])

    return resultados


datos_transacciones = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

print(procesar_transacciones(datos_transacciones))