class Apresentar:
    def __init__( self, nomeCompleto ):
        self.nomeCompleto = nomeCompleto
    #Aqui estou declarando método apresenta#
    def apresenta01( self ):
        return "Ola estou me apresentando"
    def apresenta( self, nome ):
        return "Ola eu sou {0}".format(nome)
    def apresentaComAtrib( self ):
        return "Ola eu sou {0} com atributo".format(self.nomeCompleto)
#Aqui inicia nosso programa
meApresento = Apresentar("Steven Jobs")
print(meApresento.apresenta("Renan Ribeiro"))
print(meApresento.apresenta01())
print(meApresento.apresentaComAtrib())
meApresento.nomeCompleto = "Albert Einstein"
print(meApresento.apresentaComAtrib())


