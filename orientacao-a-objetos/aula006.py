# Atributo de classe

class Pessoa:

    # Atributo de Classe
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

pessoa1 = Pessoa(nome='Renan', idade=2023)


modificando_valor_do_atributo_da_classe = Pessoa.ano_atual = 1

print(modificando_valor_do_atributo_da_classe)
print(pessoa1.get_ano_nascimento())
    