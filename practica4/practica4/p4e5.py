# Marat-Rafael


#Ejercicio 5
""" Pida al usuario un importe en euros y diga si el cajero automático le 	
puede dar dicho importe utilizando el mismo billete y el más grande 	
(recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5 	€).
 	
Por ejemplo: 
25 euros → “el cajero te devuelve 5 billetes de 5 euros”
 	
20 euros → “el cajero te devuelve 1 billete de 20 euros”
 	
130 euros → “el cajero te devuelve 13 billetes de 10 euros” 
"""

print ("Buenos dias, es un cajero automatico del banco fictico")
print ("Recuerda que disponemos solo de los billetes a 500, 200, 100, 50, 20, 10 y 5 euro")
importe=int(input("por favor introduce el importe a sacar: "))


if (importe%500==0):
    print ("Has pedido ",importe," cajero devolvera ",importe//500,"billete de ",500," euros ")
    
elif (importe%200==0):
    print ("Has pedido ",importe," euro, cajero devolvera ",importe//200,"billete de ",200," euros ")
    
elif (importe%100==0):
    print ("Has pedido ",importe," euro, cajero devolvera ",importe//100,"billete de ",100," euros ")

elif (importe%50==0):
    print ("Has pedido ",importe," euro, cajero devolvera ",importe//50,"billete de ",50," euros ")
    
elif (importe%20==0):
    print ("Has pedido ",importe," euro, cajero devolvera ",importe//20,"billete de ",20," euros ")
    
elif (importe%10==0):
    print ("Has pedido ",importe," euro, cajero devolvera ",importe//10,"billete de ",10," euros ")
    
elif (importe%5==0):
    print ("Has pedido ",importe," euro, cajero devolvera ",importe//5,"billete de ",5," euros ")

else:
    print ("Error, ne disponemos de billetes menor de 5 euro")