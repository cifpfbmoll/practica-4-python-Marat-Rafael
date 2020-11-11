# Marat-Rafael


#Practica 4
    #Ejercicio 1

#Pida al usuario 5 números y diga cuál es el mayor y cuál el menor.

num1=int(input("introduce numero 1: "))

num2=int(input("introduce numero 2: "))

num3=int(input("introduce numero 3: "))

num4=int(input("introduce numero 4: "))

num5=int(input("introduce numero 5: "))

mayor=int()

menor=int()

if (num1>num2 and num1>num3 and num1>num4 and num1>num5):    
    mayor=num1
elif (num2>num1 and num2>num3 and num2>num4 and num2>num5):    
    mayor=num2
elif (num3>num1 and num3>num2 and num3>num4 and num3>num5):    
    mayor=num3
elif (num4>num1 and num4>num2 and num4>num3 and num4>num5):    
    mayor=num4
elif (num5>num1 and num5>num2 and num5>num3 and num5>num4):    
    mayor=num5
else:
    print ("Error1, hay numeros mayores iguales")
    
print("el numero mayor es ",mayor)

if (num1<num2 and num1<num3 and num1<num4 and num1<num5):    
    menor=num1
elif (num2<num1 and num2<num3 and num2<num4 and num2<num5):    
    menor=num2
elif (num3<num1 and num3<num2 and num3<num4 and num3<num5):    
    menor=num3
elif (num4<num1 and num4<num2 and num4<num3 and num4<num5):    
    menor=num4
elif (num5<num1 and num5<num2 and num5<num3 and num5<num4):    
    menor=num5
else:
    print ("Error2, hay numeros menores iguales")
    
print("el numero menor es ",menor)



                
