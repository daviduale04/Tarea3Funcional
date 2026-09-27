#Nombre: Guale Neira César David
#Curso: Programacion Funcional 5/1
# TAREA #3 Nivel 3: HOFs Complejas combinadas con Closures y Lambdas
print("\nEjercicio #11:")
"""
11.- Pipeline de Mapeo y Filtrado Combinado: Crea la HOF procesar_coleccion(lista, fn_predicado, fn_transformacion) 
que combine internamente filter y map pasando expresiones lambda.
"""
def procesar_coleccion(lista: list, fn_predicado, fn_transformacion) ->list:
    elementos_filtrados = filter(fn_predicado, lista)
    elementos_transformados = map(fn_transformacion, elementos_filtrados)
    return list(elementos_transformados)

numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
#Aqui filtramos los impares>3 y los ponemoss al cuadrado
resultado = procesar_coleccion(
    numeros,
    lambda x:x>3 and x%2==0,
    lambda x:x**2
)
print("Pipeline resultado: ",resultado)

print("\nEjercicio #12:")
"""
12.- Reductor / Agrupador Personalizado: Crea la HOF agrupar_por(lista, fn_clave) que reciba una colección de diccionarios 
y los agrupe en un diccionario clave-valor basándose en el resultado de la lambda fn_clave.
"""
from functools import reduce

def agrupar_por(lista: list, fn_clave) ->dict:
    def acumulador(grupos: dict, elemento: dict) -> dict:
        clave = fn_clave(elemento)
        if clave not in grupos:
            grupos[clave] = []
        grupos[clave].append(elemento)
        return grupos

    return reduce(acumulador,lista,{})

estudiantes = [
    {"nombre":"Carlos","carrera":"Software","promedio":9.1},
    {"nombre":"David","carrera":"TICS","promedio":9.1},
    {"nombre":"Maite","carrera":"Software","promedio":8.9},
    {"nombre":"Angell","carrera":"Informatica","promedio":8},
]

grupos_carrera = agrupar_por(estudiantes,lambda item: item["carrera"])
print("Agrupados por carrera: ")
for carrera, lista_est in grupos_carrera.items():
    print(f" {carrera}:{[e['nombre'] for e in lista_est]}")


print("\nEjercicio #13:")
"""
13.- Ejecutor Repetitivo con Estado Accesible: Crea ejecutar_y_rastrear(fn_tarea, n) que retorne un closure con el 
historial de resultados de haber ejecutado fn_tarea $N$ veces.
"""
def ejecutar_y_rastrear(fn_tarea, n: int):
    #Aqui ejecutamos la funcion fn_tarea una cantidad de veces xd
    historial = [fn_tarea(i) for i in range(1, n+1)]

    def consultor_historial():
        return historial

    return consultor_historial

generador_sensores = ejecutar_y_rastrear(lambda paso: f"Lectura #{paso}: {paso *12.5} mA",4)#4 veces se repite
resultado_rastreo = generador_sensores()

print("Todo el historial de ejecuciones realizadas: ")
for item in resultado_rastreo:
    print(" ",item)
#12.5 25 37.5 50 lo que imprime

print("\nEjercicio #14:")
"""
14.- Compositor de Cadenas de Operaciones: Crea la HOF componer_dos(f, g) que devuelva un closure que aplique $f(g(x))$, 
permitiendo encadenar transformaciones complejas en línea.
"""
def componer_dos(f,g):
    def funcion_compuesta(x):
        return f(g(x))
    return funcion_compuesta

descontar_20 = lambda precio: precio *0.80
aplicariva = lambda subtotal: subtotal *1.15

calcular_precio_fin = componer_dos(aplicariva,descontar_20)
precio_base =120
total_final = calcular_precio_fin(precio_base)#pasamos el dato

print(f"Precio original ${precio_base}")
print(f"Precio final tras f(g(x))> ${total_final:.2f}")

print("\nEjercicio #15:")
"""
15.- Decorador / HOF de Profiling y Auditoría: Crea la HOF auditar_ejecucion(fn_objetivo, fn_logger) que mida el tiempo 
y envíe el informe execution al closure/lambda de logging pasado por parámetro.
"""
import time

def auditar_ejecucion(fn_objetivo, fn_logger):
    def ejecutor_auditado(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = fn_objetivo(*args, **kwargs)
        fin = time.perf_counter()
        duracion_ms = (fin - inicio) * 1000

        # Envía el informe estructurado a la función de logging inyectada
        fn_logger(fn_objetivo.__name__, duracion_ms, resultado)
        return resultado

    return ejecutor_auditado

# Función objetivo de prueba
def suma_pesada(limite: int) -> int:
    return sum(range(limite))

# Lambda para formatear y reportar la auditoría
logger_consola = lambda fn_nom, tiempo, res: print(f"[AUDITORÍA] Función '{fn_nom}' | Tiempo: {tiempo:.4f} ms | Resultado: {res}")

tarea_auditada = auditar_ejecucion(suma_pesada, logger_consola)
salida = tarea_auditada(2_000_000)



