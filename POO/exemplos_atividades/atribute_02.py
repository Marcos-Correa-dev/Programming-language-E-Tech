class ContadorDeObjetos:
    # Atributo de Classe:
    total_objetos = 0

    def __init__(self, nome):
        self.nome =nome # Atributo de instância

        # Modifica o atributo de Classe a cada NOVA Instância
        ContadorDeObjetos.total_objetos += 1

    def exibir_contagem(self):

        print(f"Objeto {self.nome} criado. Total geral: "
              f"{ContadorDeObjetos.total_objetos}")

# Criação de Objetos e execução do Contador:
obj1 = ContadorDeObjetos("Item A")
obj1.exibir_contagem()
# saída: Objeto "Item A" criado.  Total geral: 1

obj2 = ContadorDeObjetos("Item B")
obj2.exibir_contagem()
# Saída: Objeto "Item B" cirado. Total geral: 2

# obj1 e obj2 COMPARTILHAM o mesmo contador!!!!!!!!!
