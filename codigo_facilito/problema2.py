"""Crear una lista la cual almacene 10 números positivos ingresados por el usuario, mostrar en pantalla: 
la suma de todos los números, el promedio, el número mayor y el número menor."""
lista=[]
suma=0
i=0
for x in range(10):
  x1=int(input("Ingrese un número: ")) 
  lista.append(x1)
  suma=suma+lista[i]
  i+=1
  

print("la lista es: ",lista)
print("la suma es: ",suma)
print("el promedio es: ",suma/len(lista))
print("el número máximo es: ",max(lista))
print("el número mínimo es: ",min(lista))
