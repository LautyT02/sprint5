class Direccion(object):
    def __init__(self,calle="Avenida San Martín",numero=55,ciudad="Mendoza",provincia="Mendoza",pais="Argentina") -> None:
        self.calle=calle
        self.numero=numero
        self.ciudad=ciudad
        self.provincia=provincia
        self.pais=pais

    def __str__(self) -> str:
        _str="\t"+'"direccion": { \n'
        _str+="\t \t"+'"calle": "' + self.calle + '", \n'
        _str+="\t \t"+'"numero": "' + str(self.numero) + '", \n'
        _str+="\t \t"+'"ciudad": "' + self.ciudad + '", \n'
        _str+="\t \t"+'"provincia": "' + self.provincia + '", \n'
        _str+="\t \t"+'"pais": "' + self.pais + '"\n'
        _str+="\t }"
        return _str