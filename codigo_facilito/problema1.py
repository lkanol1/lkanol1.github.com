"""Dado un diccionario, el cual almacena las calificaciones de un alumno, siendo las llaves los nombres de las materia y los valores las calificación, mostrar en pantalla el promedio del alumno.
Ejemplo: calificaciones = {calculo:10, dibujo:5}"""

cal_alumno={'Matemática básica':14,'Programación estructurada':13,'Metodología de la investigación':12,"ciencias":16}

"""A partir del diccionario del ejercicio anterior, mostrar en pantalla la materia con mejor promedio."""

cal=dict(zip(cal_alumno.values(),cal_alumno.keys()))
#el zip devuelve un objeto de tipo tupla con eso dos elementos mostrados
#lo que hacemos es volverlo a diccionario y asi ya tenemos las notas
#como llaves y luego sacamos el max
maxi=max(cal)
suma=0


for promedio in cal_alumno.values():

	suma=suma+promedio

promedio=suma/len(cal_alumno)

print(promedio)
print(cal[maxi])


