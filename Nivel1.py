#Nombre: Guale Neira César David
#Curso: Programacion Funcional 5/1
# TAREA #3  Nivel 1: Closures con Inyección de Comportamiento (Lambdas + Closures)
print("\nEjercicio #1:")
"""
1.- Generador de Formateadores con Transformación: Crea crear_formateador(prefijo, fn_transformacion) 
que devuelva un closure. La función devuelta debe procesar un texto aplicando la lambda/función 
fn_transformacion y concatenar el prefijo.
"""
def crear_formateador(prefijo,fun_transformacion):
    def formateador(texto: str) -> str:
        texto_procesado = fun_transformacion(texto)
        return f"El prefijo {prefijo}, el texto procesado {texto_procesado}"
    return formateador

formatear_error = crear_formateador("[ERROR] ", lambda t: t.upper())
resultado = formatear_error("conexion fallida")
print(resultado)#Sale imprimendo ERROR + Concexion fallida

print("\nEjercicio #2:")
"""
2.- Multiplicador Paramétrico con Mapeo: Crea crear_operador(factor, operacion_lambda) que devuelva un 
closure capaz de aplicar la operación recibida utilizando el factor encapsulado.
"""
def crear_operador(factor, operacion_lambda):
    def operador(numero: float) -> float:
        resultado_operacion = operacion_lambda(numero, factor)
        return resultado_operacion
    return operador

duplicar = crear_operador(2, lambda x, f: x *f)
resultado = duplicar(25)
print(resultado)#50 sale

print("\nEjercicio #3:")
"""
3.- Calculador de Descuentos con Regla Dinámica: Crea crear_descuento_dinamico(regla_condicional_lambda) 
que devuelva un closure. Este evaluará el precio con la lambda enviada para determinar si aplica un 
descuento prefijado.
"""
def crear_descuento_dinamico(regla_condicional_lambda):
    porcentaje_descuento = 0.10  # Descuento prefijado del 10%
    def calculador(precio: float) -> float:
        if regla_condicional_lambda(precio):
            return precio * (1.0 - porcentaje_descuento)
        return precio
    return calculador

descuento_compras_grandes = crear_descuento_dinamico(lambda p: p > 100)
resultado_sin_descuento = descuento_compras_grandes(80)
resultado_con_descuento = descuento_compras_grandes(150)
print(f"Total sin descuento ${resultado_sin_descuento}")
print(f"Total con descuento ${resultado_con_descuento}")

print("\nEjercicio #4:")
"""
4.- Generador de Seriales / Nombres Únicos: Crea crear_generador_sufijos(patron_lambda) que devuelva un 
closure para transformar nombres de archivos basándose en una lambda de formato.
"""
def crear_generador_sufijos(patron_lambda):
    def generador(nombre_base: str, identificador) -> str:
        sufijo = patron_lambda(identificador)
        return f"{nombre_base}{sufijo}"
    return generador

generar_version_txt = crear_generador_sufijos(lambda v: f"_v{v:03d}.txt")
nombre_archivo = generar_version_txt("reporte_mensual", 4)
print(nombre_archivo)

print("\nEjercicio #5:")
"""
5.- Conversor de Divisas con Margen: Crea crear_conversor(tasa, margen_lambda) que retorne una función para 
convertir montos calculando dinámicamente la comisión adicional.
"""
def crear_conversor(tasa, margen_lambda):
    def conversor(monto: float) -> float:
        monto_convertido = monto * tasa
        comision = margen_lambda(monto)
        return monto_convertido + comision
    return conversor

conversor_eur_usd = crear_conversor(1.08 , lambda m: 2.0 if m<50 else m*0.015)
#Tasa de 1.08 + comision de $2 fijos

total_pago = conversor_eur_usd(100)
print(f"Total a pagar en Dolares ${total_pago}")