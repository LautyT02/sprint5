from .cheque import Cheque

class Chequera(object):
    def __init__(self) -> None:
        self.cheques=[]

    def agregarCheque(self,cheque=Cheque()):
        self.cheques.append(cheque)
