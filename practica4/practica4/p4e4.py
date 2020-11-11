# Marat-Rafael
#Practica 4
    #Ejercicio 4
"""Pida al usuario tres números y un cuarto número, y compruebe si este último 
es divisor de los tres números primeros."""

print ("divisores de un numero natural son los numeros naturales que pueden \
dividir, resultando de cociente otro numero natural y de resto 0 ") 

num1=int(input("introduce por favor primer numero natural: "))

num2=int(input("introduce por favor segundo numero natural: "))

num3=int(input("introduce por favor tercer numero natural: "))

divisor=int(input("introduce un numero natural para ver si es divisor de los tres \
numeros anteriores\n"))

#dividimos en primer numero y veremos si hay resto o no
if (num1%divisor==0):
    print (" El numero ",divisor," es divisor del numero ",num1)
else:
    print (" El numero ",divisor," no es divisor del ",num1)
    
    
#dividimos en segundo numero
if (num2%divisor==0):
    print (" El numero ",divisor," es divisor del numero ",num2)
else:
    print (" El numero ",divisor," no es divisor del ",num2)

#dividimos en tercer numero
if (num3%divisor==0):
    print (" El numero ",divisor," es divisor del numero ",num3)
else:
    print (" El numero ",divisor," no es divisor del ",num3)
    


