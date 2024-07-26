#Variables
entero = 8
flotante = 9.8
cadena = "Hola mundo"
Cadena = "Otro valor"
print(entero)
print(cadena)
print(Cadena)
entero = "Esto ahora es una cadena"
print(entero)

#if
x = 10
if x > 5:
    print("x es mayor a 5")

#if else
y = 3
if y > 5:
    print("y es mayor a 5")
else:
    print("y es menor que 5")

#if elif else
z = 2
if z >= 10:
    print("z es mayor a 10")
elif z <= 3:
    print("z es menor 3")
else:
    print("z esta entre 3 y 10")

#Funciones
def Saludar():
    print("Hola a todos")

Saludar()


def saludar(nombre, apellido):
    print("Hola "+nombre+ " "+ apellido+"!")
saludar("Dayana", "Reyes")

def sumar(valor1, valor2):
    print( valor1 + valor2)

sumar(5,3)


def saludo(nombre = "Pablo"):
    print("Hola "+nombre)

saludo()
saludo("Oliver")



def aplicar_funcion(funcion, valor):
    return funcion(valor)

def cuadrado(x,y=2):
    return x*y

def suma(x):
    return x+x
resultado = aplicar_funcion(cuadrado, 4)
resultado2 = aplicar_funcion(suma, 1)
print(resultado)
print(resultado2)

#Iteracion
#for
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)

for numero in range(5):
    print(numero)

#while
contador = 3
while contador < 5:
    print(contador)
    contador += 1

#String
cadena = "Prueba"
print(cadena.lower())
print(cadena.upper())


#metodo str.format()

nombre = "Abel"
edad = 21
print("Mi nombre es {} y tengo {} años".format(nombre, edad))

#F-String
nombre = "Dayana"
edad = 22
print(f"Mi nombre es {nombre} y tengo {edad} años")


cadena = "Hola Hola Adios Hola"
conteo = cadena.count("Adios")
print(conteo)

texto = "Hola y Adios"
if "Adios" in texto:
    print("Si hay un adios")
else:
    print("No hay un adios")

#Acceso caracteres
cadena = "python"
print(cadena[0])
print(cadena[-1])

#Longitud
print(len(cadena))

print(cadena[0:2])
print(cadena[2:])
print(cadena[:4])
print(cadena[1:5])




