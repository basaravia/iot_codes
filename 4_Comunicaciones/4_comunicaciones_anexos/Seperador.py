#!/usr/bin/python3
__author__ = "Alexander Saravia"
__copyright__ = "Alexander Saravia, 2019"
__credits__ = ["Alexander Saravia", "alguien mas"]
__license__ = "CC BY-NC-SA 4.0"
__version__ = "1.0.0"
__maintainer__ = "Alexander Saravia"
__email__ = "alexandersaravia@protonmail.com"
__status__ = "Development"

'''
Este es un separador de mensajes separados por comas en una trama por comunicacion digital
'''
s = "144,1231693144,26959535291011309493156476344723991336010898738574164086137773096960,26959535291011309493156476344723991336010898738574164086137773096960,1.00,4295032833,1563,2747941 288,1231823695,26959535291011309493156476344723991336010898738574164086137773096960,26959535291011309493156476344723991336010898738574164086137773096960,1.00,4295032833,909,4725008"
valores=s.split(',')
for i in range(len(valores)):
    print valores[i]