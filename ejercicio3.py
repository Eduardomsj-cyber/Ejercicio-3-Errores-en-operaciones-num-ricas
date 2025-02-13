# Importante: No se importan librerías porque las operaciones básicas se pueden hacer con Python puro.

# Definimos una función para calcular los errores absoluto, relativo y porcentual entre dos valores dados.
# La función recibe tres argumentos:
# - x: Primer valor.
# - y: Segundo valor.
# - valor_real: Valor considerado como referencia para calcular el error.
def calcular_errores(x, y, valor_real):
    """
    Calcula la diferencia entre dos valores y evalúa los errores absoluto, relativo y porcentual.

    Parámetros:
    x (float): Primer valor.
    y (float): Segundo valor.
    valor_real (float): Valor real esperado.

    Retorna:
    tuple: (error absoluto, error relativo)
    """
    
    # Paso 1: Calculamos la diferencia entre x e y
    diferencia = x - y  # Restamos y a x para obtener cuánto difieren ambos valores.

    # Paso 2: Calculamos el error absoluto.
    # El error absoluto se define como el valor absoluto de la diferencia entre el valor real y la diferencia calculada.
    error_abs = abs(valor_real - diferencia)  

    # Paso 3: Calculamos el error relativo.
    # El error relativo es el cociente entre el error absoluto y el valor real.
    # Se usa abs(valor_real) para evitar divisiones por números negativos que podrían dar interpretaciones erróneas.
    error_rel = error_abs / abs(valor_real)  

    # Paso 4: Calculamos el error porcentual.
    # Se multiplica el error relativo por 100 para expresarlo en porcentaje.
    error_pct = error_rel * 100  

    # Imprimimos los resultados de cada cálculo para que el usuario vea los valores obtenidos.
    print(f"Diferencia: {diferencia}")  # Muestra cuánto difieren x e y.
    print(f"Error absoluto: {error_abs}")  # Muestra el error absoluto.
    print(f"Error relativo: {error_rel}")  # Muestra el error relativo.
    print(f"Error porcentual: {error_pct}%")  # Muestra el error en porcentaje.

    # Retornamos el error absoluto y el error relativo como una tupla.
    return error_abs, error_rel  


# Definimos una lista de valores de prueba.
# Cada elemento de la lista es una tupla que contiene tres valores:
# - El primer valor (x) y el segundo valor (y) son los números que queremos comparar.
# - El tercer valor es el valor real esperado, que se usa como referencia para calcular los errores.
valores = [
    (1.0000001, 1.0000000, 0.0000001),  # Caso 1: Diferencia pequeña entre x e y.
    (1.000000000000001, 1.000000000000000, 0.000000000000001)  # Caso 2: Diferencia aún más pequeña.
]

# Iteramos sobre la lista de valores de prueba para calcular los errores en cada caso.
for x, y, real in valores:
    print(f"\nPara x={x}, y={y}:")  # Imprimimos los valores actuales que se están evaluando.
    calcular_errores(x, y, real)  # Llamamos a la función para calcular los errores con estos valores.
