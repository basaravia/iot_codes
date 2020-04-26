#!/usr/bin/python3
__author__ = "JAOR Software - https://www.youtube.com/playlist?list=PLJy7--EGFrT3KZVWWDJGFudvVXYKiAa0S"

# Clase 40 time II

print("Clase 40 time II")
print()

# En esta clase veremos otro módulo que nos ofrece python para el manejo de la
# fecha y la hora y que es: datetime.


# Importamos la librería 
from datetime import datetime, date

# Obtenemos la fecha de hoy
xFechaHoy = date.today()

# Imprimimos la Fecha
print ("La Fecha de Hoy con today: ",xFechaHoy)
print ("Tipo de Dato             : ",type(xFechaHoy))
print ()

# Imprimimos con Formato
print ("Fecha con Formato:")
print (xFechaHoy.strftime("Fecha :%m-%d-%y. %d %b %Y es %A.  %w %W."))
print ()

# Lista de Formatos
# %a	Nombre local abreviado de día de semana
# %A	Nombre local completo de día de semana
# %b	Nombre local abreviado de mes
# %B	Nombre local completo de mes
# %c	Representación local de fecha y hora
# %d	Día de mes [01,31]
# %H	Hora (horario 24 horas) [00,23]
# %I	Hora (horario 12 horas) [01,12]
# %j	Número de día del año [001,366]
# %m	Mes [01,12]
# %M	Minuto [00,59]
# %p	Etiqueta AM o PM
# %S	Segundo
# %U	Nº semana del año. Se considera al Domingo como primer día de semana [00,53]
# %W	Nº semana del año (Se considera al Lunes como primer día de semana) [00,53]
# %x	Fecha local
# %X	Hora local
# %y	Año en formato corto [00,99]
# %Y	Año en formato largo
# %Z	Nombre de Zona Horaria

# Creando una nueva fecha
xFechaNueva = date(1965,9,16)
print ("Fecha creada con date")
print (xFechaNueva.strftime("Fecha :%m-%d-%Y \nFecha Descriptiva: %d de %b del Año %Y \nDia Semana:%j\nSemana:%U"))
print ()

#  Calcula diferencia
xDiasTranscurridos= xFechaHoy - xFechaNueva
print ("Calculamos diferencia")
print ("Transcurridos hasta hoy desde",xFechaNueva)
print (xDiasTranscurridos)
print ("Dias         :",xDiasTranscurridos.days)
print ("Segundos     :",xDiasTranscurridos.seconds)
print ("Microsegundos:",xDiasTranscurridos.microseconds)
print ("Tipo de Dato :",type(xDiasTranscurridos))
print ()

# Obtenemos la Fecha de Hoy con now
fecha1 = datetime.now()

# Creamos una fecha específica
fecha2 = datetime(1995, 11, 5, 10, 20,30,40)

# Obtenemos la diferencia
diferencia = fecha1 - fecha2

# Desplegamos 
print ("Creamos fecha con now y con datetime")
print ("Fecha1:", fecha1," Clase :",type(fecha1))
print ("Fecha2:", fecha2," Clase :",type(fecha2))
print ("Diferencia:", diferencia, "Clase:",type(diferencia))
print ("Entre las 2 fechas hay ")
print ("Días          :", diferencia.days)
print ("Segundos      :", diferencia.seconds)
print ("MicroSegundos :", diferencia.microseconds)
print ()
