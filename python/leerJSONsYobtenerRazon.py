
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
print(str(dir_obj))
tipos_cliente={"CLASSIC": Classic(data["nombre"],data["apellido"],data["numero"],data["dni"],dir_obj,190),
"GOLD": Gold(data["nombre"],data["apellido"],data["numero"],data["dni"],dir_obj,190),
"BLACK": Black(data["nombre"],data["apellido"],data["numero"],data["dni"],dir_obj,190)}
cliente=tipos_cliente[data["tipo"]]
print("tipoCliente: ",cliente.tipoCliente)
for transaccion in data["transacciones"]:
    cliente.agregarTransaccion(transaccion)

print(str(cliente))

    

