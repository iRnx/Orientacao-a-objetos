class Animal:

    # Isso é atributo de classe
    # nome = 'Leao'

    def __init__(self, nome) -> None:
        self.nome = nome 


    def comendo(self, alimento):
        return f"{self.nome} está comendo {alimento}"

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal(nome='Leão')

print(leao.executar('Arroz'))

