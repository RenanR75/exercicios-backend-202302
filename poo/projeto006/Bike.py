import Veiculo
class Bike ( Veiculo.Veiculo):
    def __init__(self, chassi, marca, modelo, ano, potencia, tipoBike):
         super().__init__(chassi, marca, modelo, ano)
         super().set_tipo("Bike")
         self.potencia = potencia
         self.tipoBike = tipoBike
         self.marcha = 0
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 0
    def bateria( self, cargaBateria ):
        if cargaBateria == 0:
            print("A Ebike só anda pedalando")
        else:
            print("A Ebike anda por si")
""" Aqui comeca o teste """
Ebike = Bike('2210092Z', 'Caloi', 'Explorer Comp', 2021, 500, 'Eletrico')
print(Ebike.get_tipo())
print(Ebike.potencia)
print(Ebike.tipoBike)
print
Ebike.bateria(50)


