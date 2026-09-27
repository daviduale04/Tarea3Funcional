#Nombre: Guale Neira César David
#Curso: Programacion Funcional 5/1
# TAREA #3 Nivel 2: Estado Encapsulado Avanzado (nonlocal + Lambdas
print("\nEjercicio #6:")
"""
6.- Contador Ponderado: Crea crear_contador_paso(fn_paso) que incremente su estado interno 
utilizando una lambda fn_paso(cuenta_actual) en lugar de un incremento fijo.
"""
def crear_contador_paso(fn_paso):
    cuenta_act = 0
    def contador():
        nonlocal cuenta_act
        cuenta_act = fn_paso(cuenta_act)
        return cuenta_act
    return contador

contado_exponencial = crear_contador_paso(lambda c: c +2 if c<6 else c*2)
print("Paso 1.-",contado_exponencial())
print("Paso 2.-",contado_exponencial())
print("Paso 3.-",contado_exponencial())
print("Paso 4.-",contado_exponencial())

print("\nEjercicio #7:")
"""
7.- Acumulador con Filtro de Aceptación: Crea crear_acumulador_validado(criterio_lambda) 
que mantenga un total acumulado privado, pero solo sume los valores que superen la prueba 
de la lambda enviada.
"""
def crear_acumulador_validado(criterio_lambda):
    total_acumulador = 0
    def acumulador(valor: float) ->float:
        nonlocal total_acumulador
        if criterio_lambda(valor):
            total_acumulador+=valor
        return total_acumulador
    return acumulador
        
#Acumulamos numeros pares positivos
acumulador_pares = crear_acumulador_validado(lambda x:x>0 and x%2==0)
print("Suma 4 que es valido: ",acumulador_pares(4))
print("Suma 5 que es rechazado: ",acumulador_pares(5))
print("Suma -2 que es rechazado: ",acumulador_pares(-2))
print("Suma 6 que es valido: ",acumulador_pares(6))

print("\nEjercicio #8:")
"""
8.- Promediador con Eliminación de Valores Extremos: Crea crear_promediador_filtrado(filtro_ruido_lambda) 
que acumule datos privadamente pero aplique la lambda para descartar valores atípicos antes de r
ecalcular el promedio.
"""
def crear_promediador_filtrado(filtro_ruido_lambda):
    datos_validos = []

    def promediador(nuevo_valor: float):
        nonlocal datos_validos
        if filtro_ruido_lambda(nuevo_valor):
            datos_validos.append(nuevo_valor)

        if not datos_validos:
            return 0.0

        promedio = sum(datos_validos) / len(datos_validos)
        return promedio

    return promediador

# Acepta únicamente valores dentro de un rango realista de notas/sensores (entre 0 y 100)
promediador_notas = crear_promediador_filtrado(lambda valor: 0 <= valor <= 100)

print("Ingresa 80 que es valido y su promedio es:", promediador_notas(80))
print("Ingresa 90 que es valido y su promedio es:", promediador_notas(90))
print("Ingresa 500 que NO es valido y su promedio es::", promediador_notas(500))
print("Ingresa 75 que es valido y su promedio es:", promediador_notas(75))

print("\nEjercicio #9:")
"""
9.- Limitador de Tasa Inteligente (Rate Limiter con Reset): Crea crear_limitador_avanzado(max_intentos, fn_alerta) 
que cuente ejecuciones privadas y ejecute fn_alerta cuando el límite sea superado.
"""
def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos_real = 0

    def limitador(accion_usuario: str):
        nonlocal intentos_real
        intentos_real +=1

        if intentos_real> max_intentos:
            return fn_alerta(intentos_real)

        return f"La accion {accion_usuario} permitida. Intento {intentos_real}/{max_intentos}"
    
    return limitador

alerta_bloqueo = lambda cuenta: f"[BLOQUEO] el limite ha sido superado, numero de intentos {cuenta}"
controlador_login = crear_limitador_avanzado(3, alerta_bloqueo)

print(controlador_login("Inicio #1"))
print(controlador_login("Inicio #2"))
print(controlador_login("Inicio #3"))
print(controlador_login("Inicio #4"))#sale error aqui pa xd y sale el limite 

print("\nEjercicio #10:")
"""
10.- Interruptor Múltiple (Máquina de Estados Ligera): Crea crear_conmutador(lista_estados) 
que alterne cíclicamente entre una lista de estados internos privados en cada llamada.
"""
def crear_conmutador(lista_estados: list):
    indice_actu = 0

    def conmutar() -> str:
        nonlocal indice_actu
        estado_seleccionado = lista_estados[indice_actu]
        #Avanzamos los indices
        indice_actu = (indice_actu +1) % len(lista_estados)
        return estado_seleccionado

    return conmutar

semaforo = crear_conmutador(["Verde","Amarillo","Rojo"])
print("Estado 1.-",semaforo())
print("Estado 2.-",semaforo())
print("Estado 3.-",semaforo())
print("Estado 4.-",semaforo()," se reinicia jaja")#Aqui se reinicia el proceso

