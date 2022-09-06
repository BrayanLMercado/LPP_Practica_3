'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 3 : Estructuras De Control De Iteración
Ejercicio 5: Realizar un programa que nos diga si cada número que tecleemos es 
             positivo o negativo, y que pare cuando tecleemos el número 0.
Fecha: 8 De Septiembre De 2022
'''
num=1
while num!=0:
    num=float(input("Captura Un Número: "))
    if num<0:
        print(num,"Es Negativo")
    else:
        print(num,"Es Positivo")

# Se usó el ciclo while ya que no se sabe cuantos números se van a capturar antes de introducir un 0