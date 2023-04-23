# O @property serve para nós chamarmos um metodo como se fosse um atributo.
# Exemplo: ao invés de chamar um método assim: caneta.get_cor(), nós chamamos assim: caneta.cor

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return self.cor_tinta

caneta = Caneta('Azul')

print(f'Cor da caneta: {caneta.cor}')
print(f'Cor da tampa: {caneta.cor_tampa}')



# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor

#     def get_cor(self):
#         return self.cor

# caneta = Caneta('Preto')

# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())














