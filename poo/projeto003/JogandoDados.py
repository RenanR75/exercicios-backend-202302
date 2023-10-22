class JogandoDados:
    """
    Classe que representara o jogo de dados para tabuleiro
    """
    def __init__(self):
        self.__numeroDeLados = 6
    def get_numeroDeLados(self):
        return self.__numeroDeLados
    def set_numeroDeLados(self,numeroDeLados):
        self.__numeroDeLados = numeroDeLados
    def jogarDado(self):
        import random as _random
        return _random.randint(0, self.__numeroDeLados)
""" Aqui inicia nosso programa """
jogar = JogandoDados()
#print(jogar.get_numeroDeLados())
#for d in range(10):
#    print(jogar.jogarDado(), end=" ")
jogar.set_numeroDeLados(9)
print(jogar.get_numeroDeLados())
for d in range(4):
    print(jogar.jogarDado(), end=" ")