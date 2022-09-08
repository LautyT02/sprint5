import json
import jsonschema
esquema={
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "numero": {
            "type": "integer"
        },
        "nombre": {
            "type": "string"
        },
        "apellido": {
            "type": "string"
        },
        "dni": {
            "type": "string"
        },
        "tipo": {
            "type": "string"
        },
        "direccion": {
            "type": "object",
            "properties": {
                "calle": {
                    "type": "string"
                },
                "numero": {
                    "type": "string"
                },
                "ciudad": {
                    "type": "string"
                },
                "provincia": {
                    "type": "string"
                },
                "pais": {
                    "type": "string"
                }
            },
            "required": [
                "calle",
                "numero",
                "ciudad",
                "provincia",
                "pais"
            ]
        },
        "transacciones": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "estado": {
                            "type": "string"
                        },
                        "tipo": {
                            "type": "string"
                        },
                        "cuentaNumero": {
                            "type": "integer"
                        },
                        "cupoDiarioRestante": {
                            "type": "integer"
                        },
                        "monto": {
                            "type": "integer"
                        },
                        "fecha": {
                            "type": "string"
                        },
                        "numero": {
                            "type": "integer"
                        },
                        "saldoEnCuenta": {
                            "type": "integer"
                        },
                        "totalTarjetasDeCreditoActualmente": {
                            "type": "integer"
                        },
                        "totalChequerasActualmente": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "estado",
                        "tipo",
                        "cuentaNumero",
                        "cupoDiarioRestante",
                        "monto",
                        "fecha",
                        "numero",
                        "saldoEnCuenta",
                        "totalTarjetasDeCreditoActualmente",
                        "totalChequerasActualmente"
                    ]
                }
            ]
        }
    },
    "required": [
        "numero",
        "nombre",
        "apellido",
        "dni",
        "tipo",
        "direccion",
        "transacciones"
    ]
}
def validarJSON(nombreArchivo):
    with open(nombreArchivo) as archivo:
            try:
                objeto = json.load(archivo)
                jsonschema.validate(objeto, esquema)
            except jsonschema.ValidationError as e:
                print('El archivo no cumple con el esquema: ', e)
            except json.decoder.JSONDecodeError as e:
                print('El archivo no tien extensión .json: ', e)