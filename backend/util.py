from backend.event_handler import EventHandler
from datetime import datetime
from pygame import quit
from time import sleep
from sys import exit
import json


def guardar_json(ruta, datos, encoding='utf-8'):
    with open(ruta, mode='w', encoding=encoding) as file:
        json.dump(datos, file, ensure_ascii=False, indent=2, separators=(',', ':'), sort_keys=True)


def abrir_json(ruta, encoding='utf-8'):
    with open(ruta, encoding=encoding) as file:
        return json.load(file)


def salir_handler(event):
    data = event.data.get('mensaje', '')
    print('Saliendo...\nStatus: ' + data)
    quit()
    exit()


def generate_id():
    sleep(0.002)
    now = ''.join([char for char in str(datetime.now()) if char not in [' ', '.', ':', '-']])
    now = now[0:-5] + '-' + now[-5:]
    return now


EventHandler.register(salir_handler, 'salir')

__all__ = [
    'guardar_json',
    'abrir_json',
    'generate_id'
]