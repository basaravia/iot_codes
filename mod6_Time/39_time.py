#!/usr/bin/python3
__author__ = "JAOR Software - https://www.youtube.com/playlist?list=PLJy7--EGFrT3KZVWWDJGFudvVXYKiAa0S"

# Clase 39 time

print("Clase 39 time")
print()

# El manejo de la Fecha y la Hora siempre es un tema especial en los lenguajes
# de programación.

# En esta clase, veremos una de las posibilidades que existen para manejar la fecha
# y la hora, y lo veremos con la librería time

# En el manejo de la información con esta librería, se hace referencia al siguiente
# dato, del cual muestro la información correspondiente:

# The Daylight Saving Time flag (tm_isdst)
#  is greater than zero if Daylight Saving Time is in effect, 
#  zero if Daylight Saving Time is not in effect, 
#  less than zero if the information is not available.

# Importamos la librería 
import time;  

# Imprimiendo la Fecha Y hora de Hoy
hoy = time.localtime()

print (hoy)
print()

print ("Año         :",hoy[0])
print ("Mes         :",hoy[1])
print ("Dia         :",hoy.tm_mday)
print ("Hora        :",hoy.tm_hour)
print ("Minutos     :",hoy.tm_min)
print ("segundos    :",hoy.tm_sec)
print ("Dia Semana  :",hoy.tm_wday)
print ("Dia del Año :",hoy.tm_yday)
print ("DST         :",hoy.tm_isdst)

print (time.asctime(hoy)) 
print ()

# Creando una Nueva Fecha
datosFecha = (1995, 3, 14, 17, 3, 38, 1, 0, 0)

# Creamos los segundosHoy
xSecNuevaFecha = time.mktime(datosFecha)

# Creamos la nueva fecha a partir de los segundosHoy
ayer = time.localtime(xSecNuevaFecha)
print(ayer)

# Desplegamos
print ("Año         :",ayer[0])
print ("Mes         :",ayer[1])
print ("Dia         :",ayer.tm_mday)
print ("Hora        :",ayer.tm_hour)
print ("Minutos     :",ayer.tm_min)
print ("segundos    :",ayer.tm_sec)
print ("Dia Semana  :",ayer.tm_wday)
print ("Dia del Año :",ayer.tm_yday)
print ("DST         :",hoy.tm_isdst)
print (time.asctime(ayer)) 
print ()

# Calculo los segundosHoy por dia
segundosPorDia = 24 * 60 * 60

# Segundos de hoy
segundosHoy = time.time()

# Fecha de hace 3 dias
segundosHace3dias = segundosHoy - (segundosPorDia * 3)

# Calculamos la Nueva Fecha
ayer = time.localtime(segundosHace3dias)
print(ayer)

# Desplegamos
print ("Año         :",ayer[0])
print ("Mes         :",ayer[1])
print ("Dia         :",ayer.tm_mday)
print ("Hora        :",ayer.tm_hour)
print ("Minutos     :",ayer.tm_min)
print ("segundos    :",ayer.tm_sec)
print ("Dia Semana  :",ayer.tm_wday)
print ("Dia del Año :",ayer.tm_yday)
print ("DST         :",hoy.tm_isdst)
print (time.asctime(ayer)) 
print ()

print (dir(time))
print (time.__loader__)
print (time.__doc__)