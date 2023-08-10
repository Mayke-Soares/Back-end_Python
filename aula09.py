class carro:
    def __init__(self, nome, marca, ano, cor, modelo, tipo, motor, potencia, classe):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.tipo = tipo
        self.motor = motor
        self.potencia = potencia
        self.classe = classe    

    def nome_carro(self):
        print(f"Caracteristicas do meu carro: nome {self.nome}")
              
    def marca_carro(self):
        print(f"marca {self.marca}")

    def ano_carro(self):    
        print(f"ano {self.ano}")
        
    def cor_carro(self):
        print(f"cor {self.cor}")
        
    def modelo_carro(self):
        print(f"modelo {self.modelo}") 
    
    def tipo_carro(self):
        print(f"tipo {self.tipo}")
    
    def motor_carro(self):
        print(f"motor {self.motor}")
        
    def potencia_carro(self):
        print(f"potência {self.potencia}")
        
    def classe_carro(self):
        print(f"classe {self.classe}")


GT5 = carro(nome="GT5", marca="mazda", ano=1982, cor="preto", modelo="hatch", tipo="automático",motor="V8", potencia=2.0, classe="não popular")

GT5.nome_carro()
GT5.marca_carro()
GT5.ano_carro()
GT5.cor_carro()
GT5.modelo_carro()
GT5.tipo_carro()
GT5.motor_carro()
GT5.potencia_carro()
GT5.classe_carro()