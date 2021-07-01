import yaml
#print("Bienvenidos al Entorno virtual")

'''var = 0
print (var == 0)
var = 1
print (var == 0)
'''

'''var = 0
print (var != 0)
var = 1
print (var != 0)
'''
'''
a = 3
b = 5
print (a > b)
'''
'''
a = 3
b = 5
c = 2
print (a <= b)
print (a <= c)
'''

#Ejemplo de input y salida bool según condición
'''n = int(input("Digite numero:"))
print(n > 100)'''

#Ejemplo hallar mayor entre dos numeros:
'''
numero1 = int(input("ingrese primer numero: "))
numero2 = int(input("ingrese segundo numero: "))

if numero1 > numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

print ("El número más grande es: ",nmasGrande)
'''

#Ejemplo Función mayor numero
'''
numero1 = int(input("ingrese primer numero: "))
numero2 = int(input("ingrese segundo numero: "))
numero3 = int(input("ingrese tercer numero: "))

nmasGrande = max(numero1, numero2, numero3)
print ("El número más grande es: ",nmasGrande)
'''
'''
#Ejemplo salida fragmento codigo
x = 1
y = 1.0
z = "1"

if x == y:
    print ("uno")
    if x == int(z):
        print ("dos")
    elif x == y:
        print ("tres")
else:
    print ("cuatro")
'''

#Ejemplo While
'''
nmasGrande = -999999999
numero = int(input("Introduzca un numero o escribe -1 para detener: "))

while numero != -1:
    if numero > nmasGrande:
        nmasGrande = numero
    numero = int(input("Introduzca un numero o escribe -1 para detener: "))
print ("El número más grande es: ", nmasGrande)
'''

#Ejemplo for
'''
for i in range (10):
    print("El valor de i actualmente es: ",i)
'''

#Ejemplo for 2
'''
for i in range (2,8):
    print("El valor de i actualmente es: ",i)
'''

#Ejemplo for 3
'''
for i in range (2,8,3):
    print("El valor de i actualmente es: ",i)
'''
#Ejemplo for 4 potenciación
'''
pow = 1
for exp in range (16):
    print ("2 a la potencia de ", exp," es: ", pow)
    pow *=2
'''
#Ejemplo break y continue
'''
#break
for i in range (1,6):
    if i == 3:
        break
    print("dentro del loop: ",i)
print ("fuera del loop")

#continue
for i in range (1,6):
    if i == 3:
        continue
    print("dentro del loop: ",i)
print ("fuera del loop")
'''

#Ejemplo operación bit a bit
'''
var = 16
varRight = var >> 1
varLeft = var << 2
print (var, varLeft, varRight)
'''
#Ejemplo operación bit a bit 2
'''
i = 15
j = 22
bit = i | j
print (bit)
'''
#Ejemplo operación bit a bit 3
x = 4
y = 1

a = x & y
b = x | y
c = ~ x
d = x ^ 5
e = x >> 2
f = x << 2
print (a, b, c, d, e, f)
print ("validacion de Git")
print ("validacion de Git 2")