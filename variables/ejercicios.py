## convenciones para nombrar una variable

## lowerCamelCase
## Se crea uniendo palabras en la que la primera letra siempre estará en minúsculas y las siguientes palabras tendrán su primera letra en mayúsculas
## . Por ejemplo, una variable que almacene el nombre de un amigo
def comprobarEstadoApi():
    pass

## UpperCamelCase
## Es similar a lowerCamelCase, pero en este caso, la primera palabra también tendrá su primera letra en mayúsculas. 
## Por ejemplo, una clase para trabajar con la API de Twitter, podríamos llamarla así:
class TwitterApi:
    pass
## snake_case
## A diferencia de los casos anteriores, aquí uniremos las palabras mediante guiones y siempre en minúsculas. 
## Usando el primer ejemplo para comprobar el estado de una API, lo escribiríamos así con este formato:
def comprobar_estado_api():
    pass
## SCREAMING_SNAKE_CASE
## En este caso, también uniremos las palabras con guiones, pero a diferencia del snake_case, 
## aquí todas las letras deberán ir en mayúsculas. Esta convención se suele utilizar para declarar constantes:
class TwitterApi:
    VERSION_API = 1
    URL_API = 'https://api.twitter.com'

## constantes y como se declara en python

## Así, para definir una constante en Python tienes que usar una variable y asumir que nunca va a cambiar.
## Para definir constantes y para poder indicar a otros programadores que un determinado valor debe ser 
## tratado como una constante es necesario utilizar la convención de que su nombre ha de ir en mayúsculas.
## De esta manera, si queremos declarar algunas constantes, como el valor del número pi, 
## el número de segundos de una hora o la anchura de un componente determinado podríamos hacer lo siguiente:
PI = 3.14592
SEGUNDOS_HORA = 3600
ANCHURA_VENTANA = 760

print(f'{PI=}')
print(f'{SEGUNDOS_HORA=}')
print(f'{ANCHURA_VENTANA=}')