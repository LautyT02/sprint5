
import json
from Modulos.validarJSONs import validarJSON
from Modulos.tipos import Classic, Gold, Black
from Modulos.direccion import Direccion

#Obtención Archivo
nombreArchivo=input('Ingrese el nombre del json a analizar: gold, classic, black: ')
print(nombreArchivo)
data=validarJSON(nombreArchivo)
#Creación Objeto Dirección
dir_dic=data["direccion"]
dir_obj = Direccion(dir_dic["calle"],int(dir_dic["numero"]),dir_dic["ciudad"],dir_dic["provincia"],dir_dic["pais"])
tipos_cliente={"CLASSIC": Classic(data["nombre"],data["apellido"],data["numero"],data["dni"],dir_obj,190),
"GOLD": Gold(data["nombre"],data["apellido"],data["numero"],data["dni"],dir_obj,190),
"BLACK": Black(data["nombre"],data["apellido"],data["numero"],data["dni"],dir_obj,190)}
cliente=tipos_cliente[data["tipo"]]
for transaccion in data["transacciones"]:
    cliente.agregarTransaccion(transaccion)
print(str(cliente))
strCliente=str(cliente)
"""
{ 
        "numero": 100001, 
        "nombre": "Nicolas", 
        "apellido": "Gaston", 
        "DNI": "29494777", 
        "tipo": "GOLD", 
        "direcccion": { 
                "calle": "Rivadavia", 
                "numero": "7900", 
                "ciudad": "Capital Federal", 
                "provincia": "Buenos Aires", 
                "pais": "Argentina"
         },
         "transacciones": [{ 
                        "estado": "ACEPTADA", 
                        "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 9000, 
                        "monto": 1000, 
                        "fecha": "10/06/2022 16:00:55", 
                        "numero": 1, 
                        "saldoEnCuenta": 100000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "No Aplica"
                }, 
                { 
                        "estado": "RECHAZADA", 
                        "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 15000, 
                        "monto": 11000, 
                        "fecha": "10/06/2022 16:40:55", 
                        "numero": 2, 
                        "saldoEnCuenta": 10000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "No posee el saldo suficiente para realizar la extracción."
                }
        ]
}
"""
"""{ 
        "numero": 100001, 
        "nombre": "Nicolas", 
        "apellido": "Gaston", 
        "DNI": "29494777", 
        "tipo": "GOLD", 
        "direcccion": { 
                "calle": "Rivadavia", 
                "numero": "7900", 
                "ciudad": "Capital Federal", 
                "provincia": "Buenos Aires", 
                "pais": "Argentina"
         }, 
        "transacciones": [{ 
                        "estado": "ACEPTADA", 
                        "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 9000, 
                        "monto": 1000, 
                        "fecha": "10/06/2022 16:00:55", 
                        "numero": 1, 
                        "saldoEnCuenta": 100000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "No Aplica"
                }, 
                { 
                        "estado": "RECHAZADA", 
                        "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 15000, 
                        "monto": 11000, 
                        "fecha": "10/06/2022 16:40:55", 
                        "numero": 2, 
                        "saldoEnCuenta": 10000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "No posee el saldo suficiente para realizar la extracción."
                }, 
                { 
                        "estado": "RECHAZADA", 
                        "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 3000, 
                        "monto": 9000, 
                        "fecha": "10/06/2022 16:55:45", 
                        "numero": 3, 
                        "saldoEnCuenta": 100000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "No posee el saldo suficiente para realizar la extracción."
                }, 
                { 
                        "estado": "RECHAZADA", 
                        "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 3000, 
                        "monto": 9000, 
                        "fecha": "10/06/2022 16:56:55", 
                        "numero": 4, 
                        "saldoEnCuenta": 100000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "No posee el saldo suficiente para realizar la extracción."
                }, 
                { 
                        "estado": "RECHAZADA", 
                        "tipo": "ALTA_TARJETA_CREDITO", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 3000, 
                        "monto": 9000, 
                        "fecha": "11/06/2022 16:00:55", 
                        "numero": 5, 
                        "saldoEnCuenta": 100000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "Alcanzó el límite de tarjetas de crédito permitido."
                }, 
                { 
                        "estado": "RECHAZADA", 
                        "tipo": "ALTA_CHEQUERA", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 3000, 
                        "monto": 9000, 
                        "fecha": "12/06/2022 16:00:55", 
                        "numero": 6, 
                        "saldoEnCuenta": 100000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "Alcanzó el límite de Chequeras permitido."
                }, 
                { 
                        "estado": "RECHAZADA", 
                        "tipo": "COMPRA_DOLAR", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 3000, 
                        "monto": 9000, 
                        "fecha": "13/06/2022 10:00:00", 
                        "numero": 7, 
                        "saldoEnCuenta": 1000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "No posee Caja de Ahorro en Dolares."
                }, 
                { 
                        "estado": "RECHAZADA", 
                        "tipo": "TRANSFERENCIA_ENVIADA", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 3000, 
                        "monto": 100000, 
                        "fecha": "14/06/2022 16:00:55", 
                        "numero": 8, 
                        "saldoEnCuenta": 100000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "No posee el saldo suficiente para realizar la transeferencia."
                }, 
                { 
                        "estado": "ACEPTADA", 
                        "tipo": "TRANSFERENCIA_RECIBIDA", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 3000, 
                        "monto": 9000, 
                        "fecha": "20/06/2022 16:00:55", 
                        "numero": 9, 
                        "saldoEnCuenta": 100000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "No Aplica"
                }, 
                { 
                        "estado": "RECHAZADA", 
                        "tipo": "TRANSFERENCIA_RECIBIDA", 
                        "cuentaNumero": 190, 
                        "cupoDiarioRestante": 3000, 
                        "monto": 600000, 
                        "fecha": "21/06/2022 16:00:55", 
                        "numero": 10, 
                        "saldoEnCuenta": 100000, 
                        "totalTarjetasDeCreditoActualmente": 1, 
                        "totalChequerasActualmente": 1, 
                        "razon": "El monto supera el límite establecido."
                }, 
        ]
 }"""
"""{
    "nombre": "JUAN",
    "apellido": "PEREZ",
    "numero": 5
}"""
transaccionesJSON= json.loads(strCliente)
print(transaccionesJSON)

    

