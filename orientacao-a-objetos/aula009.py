"""
Métodos de classe + factories(fábricas) são métodos onde "self" será "cls", ou seja,
ao invés de receber a instância no primeiro parâmetro, recebemos
a própria classe.
"""

class Pessoa:

    ano = 2023 # Atributo de classe


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
    

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa(nome='Renan', idade=24)
print(p1.nome, p1.idade)

p2 = Pessoa.criar_com_50_anos('Voldemort')
print(p2.nome, p2.idade)

p3 = Pessoa('Anônima', 23)
print(p3.nome, p3.idade)

p4 = Pessoa.criar_sem_nome(21)
print(p4.nome, p4.idade)

# print(Pessoa.ano)
# Pessoa.metodo_de_classe()










