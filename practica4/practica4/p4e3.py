# Marat-Rafael


#Practica 4 
    #Ejercicio 3
""" Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, 
y pida los datos según que caso y muestre el resultado. """

#Con if eligimos calcular triangulo o cuadrado

print ("Para calcular area elige una figura")
figura=int(input("pulsa 1 si es triangulo, pulsa 2 si es cuadrado: "))

if (figura==1):
    
    print ("has eligido triangulo")
    
    print ("para calcular area del triangulo tiene que introducir 'base' y 'altura'\n")
    
    base_tri=int(input("Introduce por favor la base del triangulo\n"))
    
    altura_tri=int(input("Introduce por favor la altura del triangulo\n"))
    
    area_tri=(base_tri*altura_tri)/2
    
    print ("La area del triangulo con la base ",base_tri," y altura "\
    ,altura_tri," es ",area_tri)
    
    
elif (figura==2):
    
    print ("has eligido cuadrado\n")
    
    print ("para calcular area del cuadrado hay que introducir lo que mide un lado\n")
    
    lado_cuad=int(input("Introduce por favor el lado del cuadrado\n"))
    
    area_cuad=lado_cuad*lado_cuad
    
    print ("la area del cuadrado con los lados ",lado_cuad," es ",area_cuad)
        
else:
    
    print("Error")
