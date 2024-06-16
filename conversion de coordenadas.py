# comentarios iniciales
print("Esta es una aplicacion para conversion de coordenadas")
print("Primero convertiremos de DMS a DD")

# conversion de latitud dms a dd
print("Ingrese los datos de la Latitud")

import math
grados = int(input("Ingrese su dato de grado:"))
minutos = int(input("Ingrese su dato de minutos:"))
segundos=float(input("Ingrese su dato de segundos:"))
min1= segundos/60 * minutos
print(min1)
grados1= round(((min1)/60 + grados),4)
print(grados1)
print("respuesta:", grados1,"°")

# conversion de longitud dms a dd
print("Ingrese los datos de la Longitud")

import math
grados = int(input("Ingrese su dato de grado:"))
minutos = int(input("Ingrese su dato de minutos:"))
segundos=float(input("Ingrese su dato de segundos:"))
min1= segundos/60 * minutos
print(min1)
grados1= round(((min1)/60 + grados),4)
print(grados1)
print("respuesta:", grados1,"°")

print("Ahora convertiremos de DD a DMS")

# conversion de latitud dd a dms

print("Ingrese los datos de la Latitud")

import math
grados = float(input("Ingrese su dato de grado con el punto decmial:"))
grados2= grados * 60
print(grados2)
minutos = int(input("Ingrese su dato de minutos, la parte decimal con el punto del resultado del inciso anterior:"))
min2= minutos * 60
print("esos son nuestro segundos:", min2,"''")
print("respuesta:", grados , grados2 , min2 )

# conversion de langitud dd a dms

print("Ingrese los datos de la Longitud")

import math
grados = float(input("Ingrese su dato de grado con el punto decmial:"))
grados2= grados * 60
print(grados2)
minutos = int(input("Ingrese su dato de minutos, la parte decimal con el punto del resultado del inciso anterior:"))
min2= minutos * 60
print("esos son nuestro segundos:", min2,"''")
print("respuesta:", grados , grados2 , min2 )
