import mensajes
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
if indice==0 and palabra=="":
    print(mensajes.error("te has hueveado eso no existe"))
else:
    print(mensajes.correcto(palabra,indice))