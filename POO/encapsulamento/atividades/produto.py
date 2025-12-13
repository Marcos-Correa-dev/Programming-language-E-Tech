class Produto:

    def __init__(self, preco):
        self.__preco = preco

    def set_preco(self, valor):
        if valor > 0:
            self.__preco = valor
            print(f"Preço alterado para: {valor}")
        else:
            print(f" Preco invalido! Não pode ser negativo ou zero")

    def get_preco(self):
        return self.__preco

produto = Produto(100)
# Tentando alterar preço para u valor negativo
produto.set_preco(-50)

# Mostrar o ´preço usando o getter
print("Preço atual:", produto.get_preco())


print(produto.__preco)