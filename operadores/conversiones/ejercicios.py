##Ejercicio
# evaluar si es menir de 17 mostrar como mensaje
#cana si es mayor a 18 mistral come y si es mayor
#a 40 mostrar ya esta usado
edad=17
if edad<18:
  print("cana")
  if edad<41:
    print("ya come")
else:
  print("ya esta usado")
## Hacer un programa que pida al usuario su dni
##si la longitud del dni es 8 que pida sus nombre
##y lo muestre por consola si la longitud del dni
##es mayor o menor a 8 que le muestre mensaje
##de error

dni=input("Ingrese su DNI: ")
if len(dni)==8:
  input("Ingrese su Nombre y Apellido: ")
else:
  print("error")

##Crear un programa qye pida al usuario ingresar su primer apellido
##tiene en como ultimos carateres las letras --ez-- mostrar un mensaje que diga eres casi español
##si los caravteres finales son --es-- que diga eres casi peruano
apellido=input("ingrese su apellido: ")
if apellido[-2:]=="ez":
  print("eres casi español")
elif apellido[-2:]=="es":
  print("eres casi peruano")
else:
  print("eres un alien")

##hacer un programa que le pida aun usuario su dni compruebe que sea de 8 digitos, si
##si es correcto que sume el primer numero y el ultimo numerodel dni, mostrar porla 
##pantalla la suma y el resultado
dnixd=input("ingrese su dni: ")
if len(dnixd)==8:
  print("es correcto")
elif dnixd==9:
  print(dni)