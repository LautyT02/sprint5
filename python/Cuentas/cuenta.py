"""
En esta clase se establecen las caracteristicas de todo cliente.
En tipos se hereda de esta clase y se modifican y agregan las caracteristicas necesarias.
""" 
class Cuenta(object):
    def __init__(self,numero,tipo):
        self.numero=numero
        self.tipo=tipo
        self.saldo=0
    
    def __str__(self) -> str:
        pass

