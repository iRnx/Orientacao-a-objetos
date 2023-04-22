import json

CAMINHO_ARQUIVO = 'aula08.json'

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa(nome='Rnx', idade=22)
p2 = Pessoa(nome='Voldemort', idade=666)
p3 = Pessoa(nome='Dumbledore', idade=1000)

bd = [p1.__dict__, p2.__dict__, p3.__dict__]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2) # json.dump irá fazer a serialização dos dados que está em objeto.


if __name__ == '__main__':
    fazer_dump()



