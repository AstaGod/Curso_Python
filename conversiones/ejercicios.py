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