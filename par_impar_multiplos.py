'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 3 : Estructuras De Control De Iteración
Ejercicio 4: Realizar un programa que capture un número e imprima si es par o impar 
             e imprima los primeros 50 múltiplos del dígito ingresado por el usuario.
Fecha: 8 De Septiembre De 2022
'''
num=int(input("Captura Un Número: "))
if num%2==0:
    print(num,"Es Número Par")
else:
    print(num,"Es Número Impar")

print("Los Primeros 50 Multiplos De",num,"Son:")

for x in range (50):
    if x==25:
        print(num*(x+1), end=" ")
        print()
    else:
        print(num*(x+1), end=" ")

#El uso de los ciclos for se debe a que ya se conoce el limite del ciclo.