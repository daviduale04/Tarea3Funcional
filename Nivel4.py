#Nombre: Guale Neira César David
#Curso: Programacion Funcional 5/1
# TAREA #3 Nivel 3: HOFs Complejas combinadas con Closures y Lambdas
print("\nEjercicio #16:")
"""
16.- Validador Compuesto de Reglas de Negocio: Crea crear_validador_múltiple(*lambdas_criterios) 
que retorne un closure que evalúe si un objeto cumple todas las reglas pasadas como argumento.
"""
def crear_validar_multiple(*lambdas_criterios):
    def validar(objeto: dict) -> bool:
        return all(criterio(objeto) for criterio in lambdas_criterios)
    return validar

es_mayor_edad = lambda u:u.get("edad",0)>=18
ingresos_suficientes = lambda u:u.get("ingresos",0)>=1200
buen_historial = lambda u:u.get("score_crediticio", 0)>=700

validar_solicitud = crear_validar_multiple(es_mayor_edad,ingresos_suficientes,buen_historial)

usuario_aprob = {"edad":24, "ingreso":1500,"score_crediticio": 752}
usuario_recha = {"edad":19, "ingreso":900,"score_crediticio": 710}

print("Solicitud #1 Aprobada?: ",validar_solicitud(usuario_aprob))
print("Solicitud #2 Aprobada?: ",validar_solicitud(usuario_recha))

print("\nEjercicio #17:")
"""
17.- Caché con Expiración o Tamaño Máximo (Memoización Profesional): Crea la HOF 
memoizar_avanzado(fn_costosa, max_items) que retorne un closure controlando el estado 
privado de una memoria caché con límite de capacidad.
"""
def memorizar_avanzado(fn_costosa, max_items: int = 3):
    cache = {}
    orden_claves = []

    def memoizada(*args):
        if args in cache:
            print(f"[CACHE HIT] recuperando para  {args}")
            return cache[args]

        print(f"[CALCULANDO] ejecutando funcion para  {args}")
        resultado = fn_costosa(*args)

        if len(cache) >= max_items:
            clave_antigua = orden_claves.pop(0)
            del cache[clave_antigua]
            print(f"[DESALOJO] cache llena, se eliminó la clave {clave_antigua}")

        cache[args] = resultado
        orden_claves.append(args)
        return resultado

    return memoizada

def factorial(n: int) -> int:
    import math
    return math.factorial(n)

calcular_factorial = memorizar_avanzado(factorial, max_items=2)
print("Resultado #5!: ",calcular_factorial(5))
print("Resultado #5! (reintento): ",calcular_factorial(5))
print("Resultado #6!: ",calcular_factorial(6))
print("Resultado #7! (fuerza desalojo de 5): ",calcular_factorial(7))
print("Resultado #5! (de nuevo vuelve a caluclar por desalojo previo): ",calcular_factorial(5))

print("\nEjercicio #18:")
"""
18.- Motor de Pipeline Secuencial (Currying / Middleware): Crea crear_pipeline(*funciones_transformacion) 
que permita pasar un dato inicial y hacerlo fluir en orden a través de todas las lambdas/funciones del pipeline.
"""
from functools import reduce

def crear_pipeline(*frunciones_transformacion):
    def pipeline(dato_inicial):
        return reduce(lambda acumulado, funcion: funcion(acumulado), frunciones_transformacion, dato_inicial)
    return pipeline

#aqui normalizamos a pipeline como un string
limpiar_espacios = lambda texto: texto.strip()
a_minusculas = lambda texto:texto.lower()
remplazar_espacios = lambda texto:texto.replace(" ","_")
sinitizar_texto = crear_pipeline(limpiar_espacios, a_minusculas, remplazar_espacios)

textocrudo = " Sistema de distribucion y redes 2026 "
textonormalizado = sinitizar_texto(textocrudo)

print("Texto original: ",f"'{textocrudo}'")
print("Texto procesado por Pipeline: ",textonormalizado)

print("\nEjercicio #19:")
"""
19.- Sistema Pub/Sub (Event Listener con HOFs y Closures): Crea crear_sistema_eventos() que 
devuelva un closure gestor capaz de registrar suscriptores (lambdas) y emitir eventos notificando a cada uno.
"""
def crear_sistema_eventos():
    suscripciones = {}

    def gestor_eventos(accion: str, evento: str, callblack_o_datos = None):
        nonlocal suscripciones

        if accion == "suscribir":
            if evento not in suscripciones:
                suscripciones[evento] = []
            suscripciones[evento].append(callblack_o_datos)
            return f"Suscripcion registrada en {evento}"

        elif accion == "emitir":
            listeners = suscripciones.get(evento, [])
            resultados= [fn(callblack_o_datos) for fn in listeners]
            return resultados

    return gestor_eventos

bus_eventos = crear_sistema_eventos()

#Registramos los listeners o lambdas para el evento
bus_eventos("suscribir","usuario_creado", lambda u:print(f"  [LOG]: Usuario {u['email']} guardado en la Base de Datos"))
bus_eventos("suscribir", "usuario_creado", lambda u: print(f" [EMAIL]: Correo de ingreso y bienvenida a {u['email']}") )

print("Emitiendo evento 'usuario_creado': ")
bus_eventos("emitir", "usuario_creado",{"email": "davidguale@upse.edu.ec"})

print("\nEjercicio #20:")
"""
20.- Mini-Query Engine sobre Listas de Objetos: Crea crear_consultor(campo) que devuelva una HOF para generar 
filtros dinámicos sobre listas de diccionarios/objetos mediante expresiones lambda complejas.
"""
def crear_consultor(campo: str):
    def generador_filtro(predicado_lambda):
        def extractor(coleccion: list) -> list:
            return [item for item in coleccion if predicado_lambda(item.get(campo))]
        return extractor
    return generador_filtro

servidores = [
    {"ip": "192.168.1.10", "cpu_uso": 85, "ram_gb": 32, "estado": "activo"},
    {"ip": "192.168.1.11", "cpu_uso": 42, "ram_gb": 16, "estado": "inactivo"},
    {"ip": "192.168.1.12", "cpu_uso": 94, "ram_gb": 64, "estado": "activo"},
    {"ip": "192.168.1.13", "cpu_uso": 15, "ram_gb": 8, "estado": "activo"}
]

consultor_cpu = crear_consultor("cpu_uso")
filtro_sobrecarga = consultor_cpu(lambda uso: uso is not None and uso > 80)

servidores_criticos = filtro_sobrecarga(servidores)

print("Servidores con CPU crítico (> 80%):")
for s in servidores_criticos:
    print(f"  Ip: {s['ip']} | CPU: {s['cpu_uso']}% | Ram: {s['ram_gb']}GB")



