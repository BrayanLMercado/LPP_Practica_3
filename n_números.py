'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 3 : Estructuras De Control De Iteración
Ejercicio 1: Realizar un programa que obtenga 
             la suma, promedio y cantidad de números de una serie de números N introducidos
             por el usuario, el programa termina cuando el usuario introduzca un 1.
Fecha: 8 De Septiembre De 2022
'''
n=0
suma=0
elementos=0
while(n!=1):
    n=float(input("Captura un número: "))
    suma+=n
    elementos+=1
prom=suma/(elementos)
print("Elementos Totales:",elementos)
print("Suma Total De Los Elementos:",suma)
print("Promedio De Los Elementos:",round(prom,5))

# Se usó el ciclo while ya que no se sabe cuantos números se van a capturar antes de introducir un 1