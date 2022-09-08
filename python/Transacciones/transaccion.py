from asyncio import current_task
from http import client
from typing_extensions import Self
from python.Clientes.cliente import Cliente
transaccionTipo={
			"estado": "ACEPTADA",
			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 9000,
			"monto": 1000,
			"fecha": "06/06/2022 10:00:55",
			"numero": 1,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 5,
			"totalChequerasActualmente" : 2
		}


class Transaccion(object):
    def __init__(self,cliente=Cliente(),transaccionDICC=transaccionTipo) -> None:
        self.cliente=cliente
        self.estado=transaccionDICC["estado"]
        self.tipo=transaccionDICC["tipo"]
        self.numeroCuenta=transaccionDICC["cuentaNumero"]
        self.cupoDiarioRestante=transaccionDICC["cupoDiarioRestante"]
        self.monto=transaccionDICC["monto"]
        self.fecha=transaccionDICC["fecha"]
        self.numero=transaccionDICC["numero"]
        self.saldoEnCuenta=transaccionDICC["saldoEnCuenta"]
        self.tarjCerdAct=transaccionDICC["totalTarjetasDeCreditoActualmente"]
        self.cheqAct=transaccionDICC["totalChequerasActualmente"]
        self.razon=""
        self.validaciones={
            "RETIRO_EFECTIVO_CAJERO_AUTOMATICO": self.validarRetiroCajero(),"ALTA_TARJETA_CREDITO": self.validarAltaTarjetaCredito(),
            "ALTA_CHEQUERA": self.validarAltaChequera(),"COMPRA_DOLAR": self.validarCompraDolares(),
            "TRANSFERENCIA_ENVIADA": self.validarTransferenciaEnviada(),"TRANSFERENCIA_RECIBIDA": self.validarTransferenciaRecibida()
            }
        if(self.estado=="RECHAZADA"):
            self.validarTrasaccion()
        
    def validarTrasaccion(self):
        self.validaciones[self.tipo]

    def validarRetiroCajero(self):
        if(self.cupoDiarioRestante<self.monto):
            self.razon+="La transacción exedería el límite de extraccion diario de $" + self.cliente.limiteExtraccion + ". "
        if(self.saldoEnCuenta<self.monto):
            self.razon="No posee el saldo suficiente para realizar la extracción. El saldo es: " + self.saldoEnCuenta + ". "

    def validarTransferenciaEnviada(self):
        if(self.saldoEnCuenta<self.monto):
            self.razon="No posee el saldo suficiente para realizar la transeferencia. El saldo es: " + self.saldoEnCuenta + ". "

    def validarTransferenciaRecibida(self):
        if(self.cliente.limTransfRecivda!=-1):
            if(self.cliente.limTransfRecivda<self.monto):
                self.razon="El monto supera el límite establecido de $" + str(self.cliente.limTransfRecivda)

    def validarAltaTarjetaCredito(self):
        if(self.cliente.cantTarjetasCredito<=self.tarjCerdAct):
            self.razon="El cliente ya alcanzó el límite de tarjetas de crédito permitido. Este es de: " + str(self.cliente.cantTarjetasCredito)

    def validarAltaChequera(self):
        if(self.cliente.cantChequeras<=self.cheqAct):
            self.razon="El cliente ya alcanzó el límite de Chequeras permitido. Este es de: " + str(self.cliente.cantChequeras)

    def validarCompraDolares(self):
        pass

        
    def __str__(self) -> str:
        diccionario='{"estado": ' + self.estado
        diccionario+=',"tipo": ' + self.tipo
        diccionario+=',"cuentaNumero": ' + str(self.numeroCuenta)
        diccionario+=',"cupoDiarioRestante": ' + str(self.cupoDiarioRestante) 
        diccionario+=',"monto": ' + str(self.monto)
        diccionario+=',"fecha": ' + self.fecha
        diccionario+=',"numero": ' + str(self.numero)
        diccionario+=',"saldoEnCuenta": ' + str(self.saldoEnCuenta)
        diccionario+=',"totalTarjetasDeCreditoActualmente": ' + str(self.tarjCerdAct)
        diccionario+=',"totalChequerasActualmente": ' + str(self.cheqAct)
        diccionario+=',razon: ' + self.razon + '}'
        return  diccionario