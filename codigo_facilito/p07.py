import datetime
from datetime import datetime, date, timedelta
hoy=datetime.now()
año_nacimiento=int(input("Ingresa el año de tu nacimiento: "))
mes_nacimiento=int(input("Ingresa el mes de tu nacimiento: "))
dia_nacimiento=int(input("Ingresa el día de tu nacimiento: "))

fecha_nacimiento=datetime(año_nacimiento,mes_nacimiento,dia_nacimiento)
meses=(int(hoy.year)-int(fecha_nacimiento.year))*12 +(int(hoy.month)-int(fecha_nacimiento.month))
c_meses=meses%12
edad=int(meses/12)


"""edad=(int(hoy.year)-int(fecha_nacimiento.year))"""
"""edad=(hoy.year-fecha_nacimiento.year)"""



print("Tú edad es: ",edad,"años"," con",c_meses,"meses",hoy.day,"días")