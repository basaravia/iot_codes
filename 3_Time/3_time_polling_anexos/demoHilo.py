import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-s) %(message)s')

def consultar(id):
    logging.info("ID: " + str(id))
    # print("Hola soy el hilo",id)
    time.sleep(2)
    return

def guardar(id,data):
    logging.info("ID: " + str(id)+ " DATA: " + str(data))
    # print("Hola soy el hilo "+str(id)+" y esta es mi data: "+str(data))
    time.sleep(5)
    return

inicio = time.localtime(time.time())

# Instanciacion de los hilos
h1 = threading.Thread(name="hilo1",target=consultar,args=(1,))
h2 = threading.Thread(name="hilo2",target=guardar,args=(2,"texto"))

# Iniciar de los hilos 
h1.start()
h2.start()

# Los hilos se deben terminar de ejecutar para que se ejecute el hilo principal
h1.join()
h2.join()
print(" >>> Soy el hilo principal ADIOS! ")

# Hilo principal
# print(" >>> HOLA! Soy el hilo principal")
# consultar(1)
# guardar(1,'demo')

fin = time.localtime(time.time())
print("Tiempo "+str(fin[5] - inicio[5]))