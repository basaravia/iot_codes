#!/usr/bin/python3
__author__ = "JAOR Software - https://www.youtube.com/playlist?list=PLJy7--EGFrT3KZVWWDJGFudvVXYKiAa0S"

# Clase 112
# Threads - Hilos 2a

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
        
        
# Crea un Objeto timer
t1 = Timer("Hora 1:",5,50)

# Iniciamos el Thread
t1.start()


# Ciclo Infinito
while True:
    # Despliega el Menu
    print("Menu")
    print("1.- Pausar")
    print("2.- Continuar")
    print("3.- Finalizar")
    
    # Lee la opción
    opcion = input("Captura la opción deseada:")
    
    # opcion 1
    if (opcion=="1"):
        # Verifica que esté corriendo
        if (t1.getCorriendo()):
            t1.setPausar()
            print("Timer ha sido Pausado ...")
        else:
            print("El timer está pausado")
            
    # opcion 2
    if (opcion=="2"):
        # Verifica que esté corriendo
        if (t1.getCorriendo()):
            print("El Timer está Corriendo")            
        else:
            t1.setContinuar()
            print("Timer Corriendo ...")                    
            
    # opcion 3
    if (opcion=="3"):
        t1.setStop()
        print("Timer Detenido ...")                 
        break
    

print("Fin del Programa Principal")
print()
