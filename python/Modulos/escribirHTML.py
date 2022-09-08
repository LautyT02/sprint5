from cgitb import html


def escribirHTML(data:dict):
    htmlFile=open(f'../paginaTransacciones/html/index.html','w')
    contenido=f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
        <title>ImprimirJSON</title>
    </head>
    <body>
        <table class="table">
            <thead>
            <tr>
                <th scope="col">Datos del Cliente</th>
                <th scope="col">Número</th>
                <th scope="col">Nombre</th>
                <th scope="col">Apellido</th>
                <th scope="col">DNI</th>
                <th scope="col">Tipo de Cliente</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row"></th>
                <td>{data["numero"]}</td>
                <td>{data["nombre"]}</td>
                <td>{data["apellido"]}</td>
                <td>{data["dni"]}</td>
                <td>{data["tipo"]}</td>
            </tr>
            </tbody>
            <thead>
            <tr>
                <th scope="col">Dirección</th>
                <th scope="col">Calle</th>
                <th scope="col">Número</th>
                <th scope="col">Ciudad</th>
                <th scope="col">Provincia</th>
                <th scope="col">Pais</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row"></th>
                <td>{data["direccion"]["calle"]}</td>
                <td>{data["direccion"]["numero"]}</td>
                <td>{data["direccion"]["ciudad"]}</td>
                <td>{data["direccion"]["provincia"]}</td>
                <td>{data["direccion"]["pais"]}</td>
            </tr>
            </tbody>
        </table>
        <table class="table">
                <thead>
                <tr>
                    <th scope="col">Transacciones</th>
                    <th scope="col">Estado</th>
                    <th scope="col">Tipo</th>
                    <th scope="col">N° Cuenta</th>
                    <th scope="col">Cupo Diario</th>
                    <th scope="col">Monto</th>
                    <th scope="col">Fecha</th>
                    <th scope="col">Saldo Cuenta</th>
                    <th scope="col">Cant. Tarjetas Crédito</th>
                    <th scope="col">Cant. Chequeras</th>
                    <th scope="col">Razón Rechazo</th>
                </tr>
                </thead>
                <tbody>
        """
    for i in range(len(data["transacciones"])):
            contenido+=f"""   
                <tr>
                    <th scope="row">{data["transacciones"][i]["numero"]}</th>
                    <td>{data["transacciones"][i]["estado"]}</td>
                    <td>{data["transacciones"][i]["tipo"]}</td>
                    <td>{data["transacciones"][i]["cuentaNumero"]}</td>
                    <td>{data["transacciones"][i]["cupoDiarioRestante"]}</td>
                    <td>{data["transacciones"][i]["monto"]}</td>
                    <td>{data["transacciones"][i]["fecha"]}</td>
                    <td>{data["transacciones"][i]["saldoEnCuenta"]}</td>
                    <td>{data["transacciones"][i]["totalTarjetasDeCreditoActualmente"]}</td>
                    <td>{data["transacciones"][i]["totalChequerasActualmente"]}</td>
                    <td>{data["transacciones"][i]["razon"]}</td>
                </tr>
                """ 
    contenido+="""
            </tbody>            
        </table>
    </body>
    </html>"""
    htmlFile.write(contenido)
    htmlFile.close()
    """
    """