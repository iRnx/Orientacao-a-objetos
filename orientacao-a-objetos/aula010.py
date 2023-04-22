"""
@staticmethod (métodos estáticos) são inúteis em Python (segundo o professor kk)
Métodos estáticos são métodos que estão dentro da classe, mas não tem acesso ao
self nem ao cls. em resumo são funções que existem dentro da sua classe.
"""

class Classe:

    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('OI', args, kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado=1)





