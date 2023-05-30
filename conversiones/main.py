##los programas se manejan de manera secuencial
## contro de flujo
#1. Condicionales
###que se realiza algo si se cumple sierta condicion
###Bloques
####Cuando nosotros utilicemos cualquier control
####de flujo o funciones el código que se debe
####ejecutar después deberá estar definida por 
####bloques identaciones
nombre="jori"
menjaje="hola bichita"
print(menjaje)
print(nombre)

##CONVERSIONES STRING NÚMEROS 
numero="10"
numeroConvertido=int(numero)
print(type(numero))
print(type(numeroConvertido))

flotanteString="10"
flotanteNumero=float(flotanteString)

print(flotanteString)
print(flotanteNumero)

numeroEntero=20
numeroString=str(numeroEntero)

print(type(numeroEntero))
print(type(numeroString))

##Ejercicios
#Aga un programa que pida al usuario su nombre
#y luego su apellido

dato1=input("ingrese su nombre: ")
dato2=input("ingrese su apellido: ")
print(f"""
==============
"{dato1}, {dato2}"
==============
""")

# hacer un programa que pida a un usuario un
#textoy me de como saluda la cantidad de letras que tiene

text1=input()
print(len(text1))