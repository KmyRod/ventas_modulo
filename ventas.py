# Módulo inicial de procesamiento de ventas

def p(d):

    res = []

    for i in d:

        if i['tipo'] == 'venta' and i['monto'] > 0 and i['estado'] == 'completado':

            if i['monto'] > 1000 or (i['cliente_tipo'] == 'VIP' and i['monto'] > 500):
                f = i['monto'] * 0.9
            else:
                f = i['monto']

            s = "Cliente: " + i['nombre'] + " - Total: " + str(f)
            res.append(s)
            print("Procesando registro de: " + i['nombre'])

        elif i['tipo'] == 'devolucion' and i['monto'] > 0:
            f = i['monto'] * -1
            s = "Cliente: " + i['nombre'] + " - Retorno: " + str(f)
            res.append(s)
            print("Procesando registro de: " + i['nombre'])

    return res

datos_sucios = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

print(p(datos_sucios))