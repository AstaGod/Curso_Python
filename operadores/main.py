#operaciones con numeros
#operadores de comparacion
mayor=12<13 #True
menor=12<15 #True
igual=12==12 #True
distinto=12!=10 #True
#operadores logicos
var = False & False #si uno es falso el resultado sera falso
opera= False | True #vasta que uno sea verdadero para que el resultado sea verdadero
#operadores aritmeticos
op=45/23/5*2
print(opera)

#ASIGNACION AUMENTADA
a=10
a+=10  ##a=a+10
##observacion
suma=True+20 
print(suma)
#True==1 y False==0
##operaciones con STRING
##convinacion de cadenas (concatenacion)
letra="hola"+" "+"a todos"

##repetir cadena
cadena="hola "*5

##obtener una cadena en espedifico
obtenerCadena="hola" 
mensaje="khskdhgkdsh dhgdhf hgfdh '@"
texto="descripcion del texot: 'esto es un texto'"
#python asigna a una cadena dos tipos de indices
##indice positivo que de izquierda a desecha
##enpiesa en 0
##el indice negarivo de derecha a izquierda
###empiesa en -1
##QUIERO IMPRIMIR LA LETRA L DE MI VARIABLE obtenerCadena

print(obtenerCadena[2])
print(mensaje[-2])
print(texto)

##troceando cadena

trocear="un mensaje"

print(trocear[2:])
print(trocear[3:6])
print(trocear[:-3])
#[inicio:final+1]
#[inicio:inicioNegativo]

ultimoString="texto largo"
ejemplo="123458"
len(ejemplo)##6
##cuanto es la catidad de indices
##indice=5
##longitud=6

longitud=len(ultimoString)
print=(ultimoString[longitud-1]) ##print(ultimoString[-1])

###pertenencia

pertenencia="hola" in "hola mundo" #Si en la izquierda tiene algo igual a la derecha sera verdadero
#y si es diferente sera falso
con="a">"A" ##codigo ASSCCI
print(pertenencia)


