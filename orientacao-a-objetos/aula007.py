# __dict__ e vars para atributos de instância

class Pessoa:

    # Atributo de Classe
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
# Todos nosso Objeto é salvo no __dict__

# p1 = Pessoa(nome='Renan', idade=2023) 

dados = {'nome': 'Renan', 'idade': 2023}
p1 = Pessoa(**dados) # Desempacotamento

# p1.__dict__['outra'] = 'Coisa'
# p1.__dict__['nome'] = 'Nome_Alterado'
# del p1.__dict__['outra']

print(p1.__dict__)
# print(vars(p1))


