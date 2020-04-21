#Dado una lista de frases ingresadas por el usuario, mostrar en pantalla todas aquellas que sean palíndromo.
"""string ="hola"[::-1]
print(string)

if string=="hola" :
	print("ga")
else:
	print("no")"""

lista=[]
n=int(input("Cuantás palabras desea ingresar en la lista:"))
i=1

while(i<=n) :

	palabra=input("ingrese una palabra: ")
	lista.append(palabra)
	i+=1

for x in lista:

	if x==x[::-1] :
		print(x,"es palindromo")
	