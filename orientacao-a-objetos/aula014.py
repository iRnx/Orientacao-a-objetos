# Encapsulamento (modificadores de acesso: public, protect, private)
# Python NÃO tem modificadores de acesso
# Mas podemos seguir as seguintes convenções

# (sem underline) = public
# pode ser acessado em qualquer lugar

# _(um underline) = protect
# Não deve ser usado fora da classe ou suas subclasses

# __(dois underlines) = private
# "name mangling" (desfiguração de nomes) em Python, só deve ser usado na classe em que foi declarado



class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'


    def metodo_publico(self):
        return 'metodo_publico'
    

    def _metodo_protected(self):
        return '_metodo_protected'
    

    def __metodo_private(self):
        return '__metodo_private'
    

f = Foo()

# privado
print(f._Foo__private)
print(f._Foo__metodo_private())

# protegido
# print(f._protected)
# print(f._metodo_protected())

# publico
# print(f.public)
# print(f.metodo_publico())
