# Módulo de procesamiento de ventas (refactorizado y documentado)

# Constantes de descuento aplicables a ventas
DESCUENTO_PORCENTAJE = 0.9
UMBRAL_DESCUENTO_ESTANDAR = 1000
UMBRAL_DESCUENTO_VIP = 500


def es_venta_valida(transaccion):
    """
    Comprueba si una transacción es una venta válida y completada.

    :param transaccion: Diccionario con los datos de la transacción.
    :return: True si es una venta válida, False en caso contrario.
    """
    return (transaccion['tipo'] == 'venta'
            and transaccion['monto'] > 0
            and transaccion['estado'] == 'completado')


def es_devolucion_valida(transaccion):
    """
    Comprueba si una transacción es una devolución válida.

    :param transaccion: Diccionario con los datos de la transacción.
    :return: True si es una devolución válida, False en caso contrario.
    """
    return (transaccion['tipo'] == 'devolucion'
            and transaccion['monto'] > 0)


def aplica_descuento(transaccion):
    """
    Calcula el monto final aplicando descuento si corresponde.
    Se aplica descuento del 10% si el monto supera el umbral estándar
    o si el cliente es VIP y supera el umbral VIP.

    :param transaccion: Diccionario con los datos de la transacción.
    :return: Monto final tras aplicar o no el descuento.
    """
    monto = transaccion['monto']
    cliente_tipo = transaccion['cliente_tipo']

    # Descuento por volumen: monto superior al umbral estándar
    if monto > UMBRAL_DESCUENTO_ESTANDAR:
        return monto * DESCUENTO_PORCENTAJE

    # Descuento especial para clientes VIP con monto superior al umbral VIP
    if cliente_tipo == 'VIP' and monto > UMBRAL_DESCUENTO_VIP:
        return monto * DESCUENTO_PORCENTAJE

    return monto


def registrar_log(nombre_cliente):
    """
    Imprime un mensaje de auditoría para registrar el procesamiento.

    :param nombre_cliente: Nombre del cliente procesado.
    :return: None
    """
    print("Procesando registro de: " + nombre_cliente)


def formatear_resultado_venta(transaccion):
    """
    Genera la cadena de texto con el resultado de una venta.

    :param transaccion: Diccionario con los datos de la transacción.
    :return: Cadena formateada con nombre del cliente y total final.
    """
    monto_final = aplica_descuento(transaccion)
    return "Cliente: " + transaccion['nombre'] + " - Total: " + str(monto_final)


def formatear_resultado_devolucion(transaccion):
    """
    Genera la cadena de texto con el resultado de una devolución.

    :param transaccion: Diccionario con los datos de la transacción.
    :return: Cadena formateada con nombre del cliente y monto de retorno negativo.
    """
    monto_retorno = transaccion['monto'] * -1
    return "Cliente: " + transaccion['nombre'] + " - Retorno: " + str(monto_retorno)


def procesar_transacciones(lista_transacciones):
    """
    Procesa una lista de transacciones de ventas y devoluciones.
    Filtra las transacciones válidas, aplica descuentos si corresponde
    y devuelve una lista de resultados formateados.

    :param lista_transacciones: Lista de diccionarios con datos de transacciones.
    :return: Lista de cadenas de texto con los resultados procesados.
    """
    resultados = []

    for transaccion in lista_transacciones:
        if es_venta_valida(transaccion):
            resultado = formatear_resultado_venta(transaccion)
            resultados.append(resultado)
            registrar_log(transaccion['nombre'])

        elif es_devolucion_valida(transaccion):
            resultado = formatear_resultado_devolucion(transaccion)
            resultados.append(resultado)
            registrar_log(transaccion['nombre'])

    return resultados


# Datos de prueba para verificar el funcionamiento del módulo
datos_transacciones = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

print(procesar_transacciones(datos_transacciones))