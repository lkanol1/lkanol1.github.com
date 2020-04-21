from collections import Counter

archivo_texto = open('../frank.txt', 'r')
texto=archivo_texto.read()
archivo_texto.close()

m=0
p=texto.replace("'","")
p=p.replace(",","")
p=p.replace("!","")
p=p.replace(".","")
p=p.replace(";","")
p=p.replace(":","")
p=p.replace("-","")
p=p.replace("?","")
p=p.lower()
p=p.split()

#contador=Counter(p)
p_frecuente=Counter(p).most_common()[0] #sacará el más común y luego contará con el counter, te
                                           #devuelve una lista dentro de una lista donde el primero
                                           #es el que más se repite

print(p_frecuente)




    





"""hola="hola mundo ss"
p=hola.split()

print(p)"""