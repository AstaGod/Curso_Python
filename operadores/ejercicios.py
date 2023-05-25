## Ejercicio uno
##  Escriba un programa que acepte el radio 
## de un círculo
## y compute su área
#Entrada=5
#SALIDA=78.5


## entradas de datos
radioCirculo=int(input("ingrese el radio del circulo: "))
## proceso
Area=3.14*(radioCirculo**2)
## salida de datos
print(f"el area del circulo es {Area}")


##ejercicio dos
##escriba un programa que acepte el radio de una esfera
##y obtenga volumen
##datos de ejemplo
##ENTRADA=5
##SALIDA =523.33333333

##Datos de entrada 
radio=int(input("ingrese el radio: "))
##proceso
Volumen=4/3*(3.14*radio**3)
##salida
print(f"el volumen de la esfera es: {Volumen}")


##ejercicio tres
##escriba un programa que acepte la base y la altura 
##de un triángulo 
## y compruebe su área
##BASE=4 ALTURA=5
##SALIDA=10.0

##Datos de entrada
Base=int(input("ingrese la base: "))
Altura=int(input("ingrese la altura: "))
##Proceso
Area=(Base*Altura)/2
##Salida
print(f"el area del triangulo es: {Area}")