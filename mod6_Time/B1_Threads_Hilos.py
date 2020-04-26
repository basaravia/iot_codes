#!/usr/bin/python3
__author__ = "JAOR Software - https://www.youtube.com/playlist?list=PLJy7--EGFrT3KZVWWDJGFudvVXYKiAa0S"

# Clase 111
# Threads - Hilos

# Importamos la librería
import threading,time

# Clase
class Timer(threading.Thread):

    def __init__(self,hora,segundos,contador):
        # Inicia el Hilo
        threading.Thread.__init__(self)
        self.hora = hora
        self.segundos = segundos
        self.contador = contador

    # El código que ejecutará el Hilo        
    def run(self):
            
        # Ciclo Infinito
        while True:
        
            # Obtiene la Hora
            hoy = time.localtime()
        
            # Imprimiendo la Hora
            print(self.hora,hoy.tm_hour,":",hoy.tm_min,":",hoy.tm_sec)
    
            # Ejecutamos un delay de segundos       
            time.sleep(self.segundos)
            
            # Decrementa Contador
            self.contador = self.contador - 1
            
            #Verifica si termina
            if (self.contador <1):
            
                print("Fin del Timer",self.hora)
                print()
                break
                
# Crea un Objeto timer
t1 = Timer("Hora 1:",5,5)

# Creamos el segundo objeto timer
t2 = Timer("Hora 2:",8,5)

# Ejecutamos los timer
t1.start()
t2.start()

x = input("Captura Algo:")
print("Lo que capturaste")
print(x)
print("Fin del Programa Principal")
print()
