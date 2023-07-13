
##bucles
#condicion=0
#while condicion<11:
    #print(condicion)
    #condicion=condicion+1

#condicion1=0
#while condicion1<21:
    #print(condicion1)
    #condicion1=condicion1+2

#edad=0
#while edad!=20:
    #edad=int(input("Ingrese su edad: "))

#nombre=""
#while nombre!="si":
    #nombre=input("Ingrese su nombre: ")

#while True:
    #nombre1=input("como te llamas: ")
    #if nombre1=="si":
       # break


#for numero in range(1,21):
    #print(numero)

#vocales=["a","e","i","o","u"]
#for numero in range(0,5):
    #print(vocales[numero])

#for vocal in vocales:
    #print(vocal)

## CREAR UNA LISTA DE CINCO COLORES CADA COLOR QUE INTERES
## TENDRAS QUE MOSTRAR POR CONSOLA SOLO CUANDO ENCUENTRE EL 
## COLOR ROJO MOSTRARA EL MENSAJE DE
## COLO ENCONTRADO Y SE TERMINARA LA EJECUCION

#colores=["negro","azul","rosa","rojo","amarillo"]
#for color in colores:
    #print(color)
    #if color == "rosa":
        #print("color encontrado")
        #break
    
#colores=["negro","azul","rosa","rojo","amarillo"]
#for color in colores:
    #if color == "rojo":
     #print("encontrado")
     #break
    #print(color)

#lista=[]
#print(lista)
#primerDato=input("ingrese una fruta: ")
#lista.append(primerDato)
#print(lista)
#segundoDato=input("ingrese una segunda fruta: ")
#lista.append(segundoDato)
#print(lista)

## crear un programa que me deje ingresar datos en una lista vacia
## en caso el usuario ingrese la palabra "si" el programa dejara
## de pedir datos y me mostrar loa lilsta con todos los datos ingresados

#lista2=[]
#while True:
    #segundato=input("ingrese una palabra: ")
    #if segundato == "si":
     
     #break
    #lista2.append(segundato)

#print(lista2)

#lista=[]
#while len (lista) < 5:
   #ingresaDato=input("ingresa un dato: ")
   #lista.append(ingresaDato)
   #print(lista)

#def llenar_espacios(texto):
    #espacios_restantes = 5 - len(texto)
    #if espacios_restantes <= 0:
        #return texto
    #else:
        #return texto + ' ' * espacios_restantes

#datos = []
#for i in range(5):
    #dato = input("Ingresa un dato: ")
    ##datos.append(llenar_espacios(dato))

#print("Datos ingresados:")
#print (datos)


# pedir al usuario un numero luego generar la tabla de multiplicar de dicho
# numero del 1 hasta el 12
#tablaDe=int(input("ingrese un numero: "))
#for numero in range(1, 13):
    #resultado=numero*tablaDe
    #print(f"{numero} * {tablaDe} = {resultado}")

# hacer un program que me pidad un numero y me calcule su factorial
#def calcular_factorial(numero):
    #if numero == 0:
        #return 0
    #else:
        #factorial = 1
        #for i in range(1, numero + 1):
            #factorial *= i
        #return factorial

#numero = int(input("Ingresa un número: "))
#factorial_resultante = calcular_factorial(numero)
#print("El factorial de", numero, "es:", factorial_resultante)

#ejemplo 2
#numero2=int(input("ingrese el numero: "))
#factorial=1
#if numero2 == 0:
    #print("el factorial de 0 es 0")
#else:
    #for num in range(1,numero2+1):
        #factorial=factorial*num
    #print(factorial)

###pedir a  un usuario una lista de 5 elementos si en la lista se ingresa o contiene la palabra disco mostrar la palabra y la ubicacion de su indice positivo

#lista=[]
#while len (lista) < 5:
   #ingresaDato=input("ingresa un dato: ")
   #lista.append(ingresaDato)
#indice=lista.index("disco")
#print(lista[indice])
#print("se encuentra en el indice numero: ",indice)

lista=[]
indice=0
palabra=""
while len (lista)<5:
    dato=input("ingrese un dato: ")
    lista.append(dato)
for texto in range(0,len(lista)):
    if lista[texto] == "disco":
        palabra=lista[texto]
        indice=texto
print(f"""el texto disco se encuentra en el indice hola {indice}
      y el texto es {palabra}""")

