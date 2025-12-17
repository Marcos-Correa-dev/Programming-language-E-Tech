class Aluno:
    def __init__(self, nome, nota):
        # Atributo privado (encapsulado)
        self.__nome = nome
        self.__nota = nota
     # GEtter:
    def get_nome(self):
        return self.__nome

    #GETTER:
    def get_nota(self):
        return self.__nota


    def set_nota(self, valor):
        if 0 <= valor <= 20:
            self.__nota = valor
            print("nota alterada com sucesso.")
        else:
            print("Nota inválida! deve está entre 0 e 10.")


# CRIAÇÂO de objeto!!!!!!!!

aluno = Aluno("Wendell", 8)

aluno.set_nota(21)  # Não altera

# acessando os dados via os GETTERS

print("Nome do aluno:", aluno.get_nome())

print("Nota do aluno:", aluno.get_nota())

