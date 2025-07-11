"""funciones definidas por el usuario"""

# Simple función sin parámetros ni retorno

def saludar():
    """Función que imprime un saludo"""
    print("¡Hola, Python!")
saludar()

# Con retorno
def saludar_con_retorno():
    """Función que retorna un saludo"""
    return "¡Hola, Python!"
print(saludar_con_retorno())

# Con un argumento
def saludar_con_argumento(nombre):
    """Función que recibe un nombre y retorna un saludo"""
    print(f"¡Hola, {nombre}!")

saludar_con_argumento("Juan")

# Con varios argumentos
def saludar_con_varios_argumentos(nombre, edad):
    """Función que recibe un nombre y una edad, y retorna un saludo"""
    print(f"¡Hola, {nombre}! Tienes {edad} años.")
saludar_con_varios_argumentos("Ana", 30)

# Con un argumento predeterminado
def saludar_con_argumento_predeterminado(nombre="amigo"):
    """Función que recibe un nombre con valor predeterminado y retorna un saludo"""
    print(f"¡Hola, {nombre}!")
saludar_con_argumento_predeterminado()
saludar_con_argumento_predeterminado("Carlos")

# Con argumentos y retorno
def saludar_con_retorno_argumento(nombre):
    """Función que recibe un nombre y retorna un saludo"""
    return f"¡Hola, {nombre}!"
print(saludar_con_retorno_argumento("Laura"))

#con retorno de varios valores
def multiple_retorno():
    """Función que retorna varios valores"""
    return "Python", 3.10, True
lenguaje, version, es_interesante = multiple_retorno()
print(f"Lenguaje: {lenguaje}, Versión: {version}, Interesante: {es_interesante}")

# Con un número variable de argumentos
def saludar_varios(*nombres):
    """Función que recibe un número variable de nombres y retorna un saludo"""
    for nombre in nombres:
        print(f"¡Hola, {nombre}!")
saludar_varios("Pedro", "María", "Luis")

# Con un numero variables de argumentos con palabra clave
def saludar_con_kwargs(**kwargs):
    """Función que recibe un número variable de argumentos con palabra clave y retorna un saludo"""
    for nombre, edad in kwargs.items():
        print(f"¡Hola, {nombre}! Tienes {edad} años.")
saludar_con_kwargs(Pedro=25, María=30, Luis=22)

""""funciones dentro de funciones"""

def outer_function():
    """Función externa que define una función interna"""
    def inner_function():
        """Función interna que imprime un mensaje"""
        print("¡Hola desde la función interna!")
    inner_function()
outer_function()

# Funciones del lenguaje (built-in functions)
"""Uso de funciones integradas del lenguaje Python"""

print(len("Hola, Python!"))  # Longitud de una cadena
print(type(42))  # Tipo de un objeto
print(max([1, 2, 3, 4, 5]))  # Valor máximo en una lista

# variables locales y globales

global_var = "Python"

print(global_var)  # Acceso a variable global

def hello_python():
    local_var = "Hola"  # Variable local
    print(f"{local_var}, {global_var}!")  # Acceso a variable global dentro de la función

hello_python()

# Ejercicio extra

def print_numbers(text_1, text_2)-> int:
    count = 0
    for nuember in range(1, 101):
        if nuember % 3 == 0 and nuember % 5 == 0:
            print(f"{text_1} {text_2}")
        elif nuember % 3 == 0:
            print(text_1)
        elif nuember % 5 == 0:
            print(text_2)
        else:    
            print(nuember)
            count += 1
    return count

print(print_numbers("Texto 1", "Texto 2"))
