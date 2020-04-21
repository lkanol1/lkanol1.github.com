#cantidad de vocales
palabra=input("Ingrese una palabra: ")

i=0
j=0
k=0
l=0
m=0
for x in palabra:
	if x=='a':
	  i+=1
	elif x=='e':
	  j+=1
	elif x=='i':
	  k+=1
	elif x=='o':
	  l+=1	
	elif x=='u':
	  m+=1  

print("veces que se repite la vocal 'a': {} \nveces que se repite la vocal 'e': {} \nveces que se repite la vocal 'i': {} \nveces que se repite la vocal 'o': {} \nveces que se repite la vocal 'u': {} \n".format(i,j,k,l,m))

