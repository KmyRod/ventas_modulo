# Módulo inicial de procesamiento de ventas

DESCUENTO_PORCENTAJE = 0.9
UMBRAL_DESCUENTO_ESTANDAR = 1000
UMBRAL_DESCUENTO_VIP = 500

def procesar_transacciones(lista_transacciones):

    resultados = []

    for transaccion in lista_transacciones:

        if transaccion['tipo'] == 'venta' and transaccion['monto'] > 0 and transaccion['estado'] == 'completado':

            if transaccion['monto'] > 1000 or (transaccion['cliente_tipo'] == 'VIP' and transaccion['monto'] > 500):
                monto_final = transaccion['monto'] * 0.9
            else:
                monto_final = transaccion['monto']

            resultado = "Cliente: " + transaccion['nombre'] + " - Total: " + str(monto_final)
            resultados.append(resultado)
            print("Procesando registro de: " + transaccion['nombre'])

        elif transaccion['tipo'] == 'devolucion' and transaccion['monto'] > 0:
            monto_final = transaccion['monto'] * -1
            resultado = "Cliente: " + transaccion['nombre'] + " - Retorno: " + str(monto_final)
            resultados.append(resultado)
            print("Procesando registro de: " + transaccion['nombre'])

    return resultados

datos_transacciones = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

print(procesar_transacciones(datos_transacciones))