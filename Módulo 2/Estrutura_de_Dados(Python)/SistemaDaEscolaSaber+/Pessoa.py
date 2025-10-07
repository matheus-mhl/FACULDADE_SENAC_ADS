#Classe pai - SuperClass()
class Pessoa:
    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        
#Criando MÉTODO
    def mostrar_detalhes(self):
        print(f'''
              --- 🤷Detalhes Pessoa ---
                    nome: {self.nome}
                    idade: {self.idade}
                    cpf: {self.cpf}
                    endereco: {self.endereco}
                    telefeone: {self.telefone}
              ''')
        
#Criando subclass
class Professor(Pessoa): #Criando subclasse PROFESSOR
    def __init__(self, nome, idade, disciplina):#Adicionando atributo DISCIPLINA
        super().__init__(nome, idade, disciplina)
        self.nome = nome
        self.idade = idade
        self.disciplina = disciplina
        
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f'''
              Nome: {self.nome}
              Idade: {self.idade}
              Disciplina: {self.disciplina}
              ''')
        
#Criando subclasse ALUNO com atributo MATRICULA
class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, endereco, telefone, matricula):
        super().__init__(matricula)
        self.matricula = matricula
        
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f'''
              Matrícula: {self.matricula}
              ''')

#Criando subclasse FUNCIONARIO com atributo CARGO
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, endereco, telefone, cargo):
        super().__init__(cargo)
        self.cargo = cargo
        
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f'''
              Cargo: {self.cargo}
              ''')