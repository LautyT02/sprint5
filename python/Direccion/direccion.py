class Direccion(object):
    def __init__(self,calle="Avenida San Martín",numero=55,ciudad="Mendoza",provincia="Mendoza",pais="Argentina") -> None:
        self.calle=calle
        self.numero=numero
        self.ciudad=ciudad
        self.provincia=provincia
        self.pais=pais

    def __str__(self) -> str:
        _str='"direcccion: "{ \n'
        _str+='"calle": ' + self.calle + ', \n'
        _str+='"numero": ' + str(self.numero) + ', \n'
        _str+='"ciudad": ' + self.ciudad + ', \n'
        _str+='"provincia": ' + self.provincia + ', \n'
        _str+='"pais": ' + self.pais + '\n'
        _str+="}"
        return _str