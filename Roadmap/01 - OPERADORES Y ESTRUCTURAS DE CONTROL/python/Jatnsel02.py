'Operadores'

# Operadores Aritmeticos
print(f"suma: 2 + 3 = {2 + 3}")
print(f"resta: 2 - 3 = {2 - 3}")
print(f"multiplicacion: 2 * 3 = {2 * 3}")
print(f"division: 2 / 3 = {2 / 3}")
print(f"division entera: 2 // 3 = {2 // 3}") # division entera
print(f"modulo: 2 % 3 = {2 % 3}") # resto de la division
print(f"exponente: 2 ** 3 = {2 ** 3}")

# Operadores de Comparacion
print(f"igual: 2 == 3 = {2 == 3}") # igualdad
print(f"desigualdad: 2 != 3 = {2 != 3}") # desigualdad
print(f"mayor: 2 > 3 = {2 > 3}") # mayor que
print(f"menor: 2 < 3 = {2 < 3}") # menor que
print(f"mayor o igual: 2 >= 3 = {2 >= 3}") # mayor o igual que
print(f"menor o igual: 2 <= 3 = {2 <= 3}") # menor o igual que

# Operadores Logicos
print(f"AND &&: 2 + 3 == 5 and 2 - 3 == -1 es {2 + 3 == 5 and 2 - 3 == -1}") # AND
print(f"OR ||: 2 + 3 == 5 or 2 - 3 == -1 es {2 + 3 == 5 or 2 - 3 == -1}") # OR
print(f"NOT !: not (2 + 3 == 5) es {not (2 + 3 == 5)}") # NOT


# Operadores de Asignacion
a = 2  # asignacion
print(a) # asignacion
a += 3 # asignacion suma
print(f"asignacion suma: a += 3, a es {a}") # asignacion suma
a -= 3 # asignacion resta
print(f"asignacion resta: a -= 3, a es {a}") # asignacion resta
a *= 3 # asignacion multiplicacion
print(f"asignacion multiplicacion: a *= 3, a es {a}") # asignacion multiplicacion
a /= 3 # asignacion division
print(f"asignacion division: a /= 3, a es {a}") # asignacion division
a //= 3 # asignacion division entera
print(f"asignacion division entera: a //= 3, a es {a}") # asignacion division entera
a %= 3 # asignacion modulo
print(f"asignacion modulo: a %= 3, a es {a}") # asignacion modulo
a **= 3 # asignacion exponente
print(f"asignacion exponente: a **= 3, a es {a}") # asignacion exponente

# Operadores de Identidad
c = 1
b = a # identidad
print(f"identidad: b = a, b es {b} y a es {a}") # identidad
print(f"b es a: {b is a}") # identidad
print(f"b no es a: {b is not a}") # identidad negada
print(f"c es a: {c is a}") # identidad
print(f"c no es a: {c is not a}") # identidad negada

# Operadores de Pertenencia
print(f"'t' in 'Jatnsel': {'t' in 'Jatnsel'}") # pertenencia
print(f"'J' not in 'Jatnsel': {'J' not in 'Jatnsel'}") # pertenencia negada

# Operadores Bit a Bit
d = 5 # 0101
e = 3 # 0011
print(f"AND bit a bit: {d} & {e} = {d & e}") # AND bit a bit
print(f"OR bit a bit: {d} | {e} = {d | e}") # OR bit a bit
print(f"XOR bit a bit: {d} ^ {e} = {d ^ e}") # XOR bit a bit
print(f"NOT bit a bit: ~{d} = {~d}") # NOT bit a bit
print(f"Desplazamiento a la izquierda: {d} << 1 = {d << 1}") # Desplazamiento a la izquierda
print(f"Desplazamiento a la derecha: {d} >> 1 = {d >> 1}") # Desplazamiento a la derecha

# Estructuras de Control

# Condicionales
my_string = "Jatnsel"
if my_string == "Jatnsel":
    print("El string es 'Jatnsel'")
elif my_string == "Jatnsel2":
    print("El string es 'Jatnsel2'")
else:
    print("El string es 'Python'")

# Interativas
# For
for i in range(6):
    print(f"Iteracion {i}")

# While
i = 0    
while i <= 6:
    print(f"Iteracion {i}")
    i += 1

# Manejo de Excepciones
try:
    print(10 / 0)
except:
    print("Error: Division por cero")
finally:
    print("Fin del manejo de excepciones")

#Ejercicio 
# Crear un programa que imprima los numeros del 10 al 56, pero si el numero es par, imprimir "Par" en su lugar
for i in range(10, 56):
    # Verificar si el numero es par
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)

