from db import mongoEngineDB

class Clientes(mongoEngineDB.Document):
    nome = mongoEngineDB.StringField()#required=True
    cpf = mongoEngineDB.StringField()
    celular = mongoEngineDB.StringField()
    score = mongoEngineDB.IntField()
    negativado = mongoEngineDB.BooleanField()

    def save(self, *args, **kwargs):
        if type(self.cpf) == int:
            self.cpf = str(self.cpf)
        
        if type(self.celular) == int:
            self.celular = str(self.celular)

        return super(Clientes, self).save(*args, **kwargs)


class Taxas(mongoEngineDB.Document):
    tipo = mongoEngineDB.StringField()
    taxas = mongoEngineDB.ListField()
