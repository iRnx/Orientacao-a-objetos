# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático sem(self) e sem(cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

# Método de instância, aqui nós temos acesso aos atributos do __init__   
c1 = Connection()
c1.set_user('Voldemort')
c1.set_password('1566666')
print(c1.user)
print(c1.password)

# Método de classe, aqui temos acesso apenas ao valor da função, sem o self. apenas o cls()
# @classmethod
c1 = Connection.create_with_auth('Bolsonaro', '1234')
print(c1.user)
print(c1.password)


