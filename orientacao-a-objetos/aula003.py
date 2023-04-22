class Carro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def acelerar(self):
        return f"{self.nome} está acelerando... VRUMMMMM VRUMMMM VRUMMMM"
    
    
p1 = Carro(str(input('Digite o nome do Carro: ')), int(input('Digite sua idade: ')))
print(f"O {p1.acelerar()}")

p2 = Carro(str(input('Digite o nome do Carro: ')), int(input('Digite sua idade: ')))
print(f"O {p2.acelerar()}")
