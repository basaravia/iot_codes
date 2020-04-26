import threading 

def timerFunc(): 
    print("Ejecuta funcion")
            
timer = threading.Timer(2.0, timerFunc) 
timer.start() 
# print("Cancelling timer\n") 
# timer.cancel()
print("Exit\n")