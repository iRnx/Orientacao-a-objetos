# getter(@property) -> obter um valor
# setter -> definir um valor


class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self._cor_tampa = None


    @property
    def cor(self):
        return self._cor
    

    @cor.setter
    def cor(self, valor):
        print('Estou no getter')

        if type(valor) == str:
            print('é string')
        else:
            raise ValueError('Aceitamos apenas string...')
        
        if valor.capitalize() == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor.capitalize()


    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Verde')
caneta.cor = 'rOXO'
caneta.cor_tampa = 'roxo'

print(f'Cor da caneta: {caneta.cor}')
print(f'Cor da tampa: {caneta.cor_tampa}')



# Chamamos o setter quando o usuário atribuir um valor ao caneta.cor = 'rosa'
# class Caneta:
#     def __init__(self, cor):
#         self._cor = cor

#     @property
#     def cor(self):
#         return self._cor
    
#     @property
#     def cor_tampa(self):
#         return self._cor
    
#     @cor.setter
#     def cor(self, valor):
#         if valor.capitalize() == 'Rosa':
#             raise ValueError('Não aceito essa cor')
#         self._cor = valor.capitalize()

# caneta = Caneta('Azul')
# caneta.cor = 'rOXO'

# print(f'Cor da caneta: {caneta.cor}')
# print(f'Cor da tampa: {caneta.cor_tampa}')