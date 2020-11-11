# Marat-Rafael

#Practica 4
    #Ejercicio 2
""" Pida al usuario 5 números y diga si estos estaban en orden decreciente, 	
creciente o desordenados. """

#variables
num1=int(input("introduce numero 1: "))

num2=int(input("introduce numero 2: "))

num3=int(input("introduce numero 3: "))

num4=int(input("introduce numero 4: "))

num5=int(input("introduce numero 5: "))

#comparamos numeros con if
if num1<num2 and num2<num3 and num3<num4 and num4<num5:
    print ("Has introducido numeros ",num1,num2,num3,num4,num5)
    print ("Estan en orden creciente")
    
elif num1>num2 and num2>num3 and num3>num4 and num4>num5:
    print ("Has introducido numeros ",num1,num2,num3,num4,num5)
    print ("Estan en orden Decreciente")
    
else:
    print ("Has introducido numeros ",num1,num2,num3,num4,num5)
    print ("Estan en orden desordenado")
    
print ("Gracias")
