import Veiculo
class Caminhao ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, potencia, eixo, tipoCaminhao):
         super().__init__(chassi, marca, modelo, ano)
         super().set_tipo("Caminhao")
         self.potencia = potencia
         self.eixo = eixo
         self.tipoCaminhao = tipoCaminhao
         self.marcha = 0
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 0
    def buzinar( self):
        print("O Caminhão está buzinando")
    def acelerar( self):
        print("O Caminhâo anda")
    def frear( self ):
        print("O Caminhâo frea")

""" Aqui comeca o teste """
CaminhaoNovo = Caminhao('9BRBLWHEXG0107721', 'Volkswagen', 'Delivery 11.180', 2017, 175, 2, 'VUC')
print(CaminhaoNovo.get_tipo())
print(CaminhaoNovo.eixo)
print(CaminhaoNovo.potencia)
print(CaminhaoNovo.tipoCaminhao)
print(CaminhaoNovo.ligar())
CaminhaoNovo.buzinar()
CaminhaoNovo.frear()
