#!/usr/bin/python3
__author__ = "JAOR Software - https://www.youtube.com/playlist?list=PLJy7--EGFrT3KZVWWDJGFudvVXYKiAa0S"

# Clase 113
# Threads - Hilos 3a
# Demonios

# Importamos la librería
import threading,time

# Clase
class Timer(threading.Thread):

    def __init__(self,hora,segundos,contador):
        # Inicia el Hilo
        threading.Thread.__init__(self)
        self.hora = hora
        self.segundos  = segundos
        self.contador  = contador
        self.corriendo = False
        self.daemon    = True

    # El código que ejecutará el Hilo        
    def run(self):
            
        # Activa corriendo
        self.corriendo = True        
        
        # Ciclo Infinito
        while True:
            
            #Verifica que haya finalizado
            if (self.contador==0):
                print("Fin del Timer",self.hora)
                print()
                break
               
            # Obtiene la Hora
            hoy = time.localtime()
            
            # Verifica si debe desplegar
            if (self.corriendo):
            
                # Imprimiendo la Hora
                print(self.hora,hoy.tm_hour,":",hoy.tm_min,":",hoy.tm_sec)
                
                # Decrementa Contador
                self.contador = self.contador - 1                             
                
                # Ejecutamos un delay de segundos       
                time.sleep(self.segundos)
        
            
                
    def setStop(self):
        self.contador = 0

    def setPausar(self):
        self.corriendo=False
                                   
    def setContinuar(self):
        self.corriendo=True
        
    def getCorriendo(self):
        return self.corriendo
        
        
# Creamos 5 timer's
t1 = Timer("Hora 1:",1,50)
t2 = Timer("Hora 2:",2,50)
t3 = Timer("Hora 3:",3,50)
t4 = Timer("Hora 4:",4,50)
t5 = Timer("Hora 5:",5,50)

# Iniciamos los timer's
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

input("Al presionar una tecla el programa y los timer's finalizaran\n")
print("Fin del Programa Principal")
print()
