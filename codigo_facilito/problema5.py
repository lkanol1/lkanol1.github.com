"""
Remplazar cada letra de una frase dada por el usuario por la posición que le
corresponde en el abecedario y mostrar el nuevo string en pantalla. (Los espacios no se remplazan) . 
Ejemplo: frase : 'Hola' salida : 815121 H(8) o(15) l(12) a(1)
"""

abecedario={ 1:'a', 2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',
             12:'l',13:'m',14:'n',15:'ñ',16:'o',17:'p',18:'q',19:'r',20:'s',21:'t',
             22:'u',23:'v',24:'w',25:'x',26:'y',27:'z'
 
            }

new_abecedario=dict(zip(abecedario.values(),abecedario.keys()))    

palabra=input("Ingrese una palabra: ")

for x in palabra :
	valor=new_abecedario.get(x)
	print(x,"-->",valor)
