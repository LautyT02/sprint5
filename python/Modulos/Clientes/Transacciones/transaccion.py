from ast import match_case
class Transaccion(object):
    
    def __init__(self,cliente:object,transaccionDICC:dict) -> None:
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
        if(self.estado=="RECHAZADA"):
            self.razonTrasaccion()
        
        
    def razonTrasaccion(self):
        match self.tipo:
            case "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                self.razonRetiroCajero()
            case "ALTA_TARJETA_CREDITO":
                self.razonAltaTarjetaCredito()
            case "ALTA_CHEQUERA":
                self.razonAltaChequera()
            case "COMPRA_DOLAR": 
                self.razonCompraDolares()
            case "TRANSFERENCIA_ENVIADA":
                self.razonTransferenciaEnviada()
            case "TRANSFERENCIA_RECIBIDA":
                 self.razonTransferenciaRecibida()
        if(self.razon==""):
            self.razon="No se encontró el motivo del rechazo"        

    def razonRetiroCajero(self):
        if(self.cupoDiarioRestante<self.monto):
            self.razon+="La transacción exedería el límite de extraccion diario." 
        if(self.saldoEnCuenta-self.monto)>-self.cliente.descubierto:
            self.razon="No posee el saldo suficiente para realizar la extracción."

    def razonTransferenciaEnviada(self):
        if(self.saldoEnCuenta-self.monto)>-self.cliente.descubierto:
            self.razon="No posee el saldo suficiente para realizar la transeferencia."

    def razonTransferenciaRecibida(self):
        if(self.cliente.limTransfRecivda!=-1):
            if(self.cliente.limTransfRecivda<self.monto):
                self.razon="El monto supera el límite establecido."

    def razonAltaTarjetaCredito(self):
        if(self.cliente.cantTarjetasCredito<=self.tarjCerdAct):
            self.razon="Alcanzó el límite de tarjetas de crédito permitido."
        if not self.cliente.puedeCrearTarjetaCredito():
            self.razon="No puede tener Tarjeta de Credito"

    def razonAltaChequera(self):
        if(self.cliente.cantChequeras<=self.cheqAct):
            self.razon="Alcanzó el límite de Chequeras permitido."
        if not self.cliente.puedeCrearChequera():
            self.razon="No puede tener Chequera"

    def razonCompraDolares(self):
        if not self.cliente.puedeComprarDolares():
            self.razon="No posee Caja de Ahorro en Dolares."
        
    def __str__(self) -> str:
        diccionario='{ \n'
        diccionario+='"estado": ' + self.estado + ", \n"
        diccionario+='"tipo": ' + self.tipo + ", \n"
        diccionario+='"cuentaNumero": ' + str(self.numeroCuenta) + ", \n"
        diccionario+='"cupoDiarioRestante": ' + str(self.cupoDiarioRestante)  + ", \n"
        diccionario+='"monto": ' + str(self.monto) + ", \n"
        diccionario+='"fecha": ' + self.fecha + ", \n"
        diccionario+='"numero": ' + str(self.numero) + ", \n"
        diccionario+='"saldoEnCuenta": ' + str(self.saldoEnCuenta) + ", \n"
        diccionario+='"totalTarjetasDeCreditoActualmente": ' + str(self.tarjCerdAct) + ", \n"
        diccionario+='"totalChequerasActualmente": ' + str(self.cheqAct) + ", \n"
        diccionario+='"razon": ' + self.razon + "\n"
        diccionario+='}'
        return  diccionario