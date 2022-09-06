"""
En esta clase se establecen las caracteristicas de todo cliente.
En tipos se hereda de esta clase y se modifican y agregan las caracteristicas necesarias.
"""
class Cliente(object):
    def __init__(self,nombre='',apellido=''):
        self.nombre=nombre
        self.apellido=apellido