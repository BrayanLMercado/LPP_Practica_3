'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 3 : Estructuras De Control De Iteración
Ejercicio 2: Realizar un programa que capture 10 números y que imprima el promedio 
             y el mayor de los números capturados.
Fecha: 8 De Septiembre De 2022
'''
suma=0
lista=[]
for x in range(10):
    num=float(input("Captura Un Número: "))
    lista.append(num)
    suma+=num

prom=suma/10
mayor=lista[0]

for t in lista:
    if t>mayor:
        mayor=t

print("El Promedio De Los Números Capturados Es:",prom)
print("El Número Mayor Es:",mayor)

#El uso de los ciclos for se debe a que ya se conoce la cantidad de elementos totales.