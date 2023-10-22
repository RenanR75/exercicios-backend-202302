class Apresentar:
    def __init__( self, nomeCompleto ):
        self.nomeCompleto = nomeCompleto
    def apresenta01( self ):
        """Aqui estou declarando método apresenta01"""
        return "Ola estou me apresentando"
    def apresenta( self, nome ):
        """Aqui estou declarando método apresenta"""
        return "Eu sou {0}".format(nome)
    def apresentaComAtrib( self ):
        """Aqui estou declarando método apresentaComAtrib"""
        return "Ola eu sou {0}, o cientista".format(self.nomeCompleto)
""" Aqui inicia nosso programa """
meApresento = Apresentar("Steven Jobs")
print(meApresento.apresenta01())
print(meApresento.apresenta("Renan Ribeiro"))
print(meApresento.apresentaComAtrib())
meApresento.nomeCompleto = "Albert Einstein"
print(meApresento.apresentaComAtrib())