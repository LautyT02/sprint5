from ..cliente import Cliente
from ...Direccion.direccion import Direccion

class Gold(Cliente):
    def __init__(self, nombre='', apellido='', numero=0, dni=11111111, direccion=Direccion(), numeroCuenta=1):
        #Datos Personales del Cliente y numeroCuenta
        super().__init__(nombre, apellido, numero, dni, direccion, numeroCuenta)
        #Cuentas
        self.cuentaAhorroDolares=True
        self.cuentaCorriente=True
        self.setDescubierto(10000)
        #Tarjetas
        self.cantTarjetasDebito=1
        self.maxTarjetasCredito=1
        #Chequeras
        self.maxChequeras=1
        #Transacciones
        self.setLimiteExtraccion(20000)
        self.setComisionTransferencia(0.005)
        self.setLimiteTransferenciaRecivida(500000)
        #Tipo de Cleinte
        self.tipoCliente='GOLD'    