class Pagamento:
    def __init__(self, valor):

        self.valor = valor

    def calcular_valor(self):
        # garante que o  polimorfismo aconteça
        return self.valor


class PagamentoCartao(Pagamento):

    def __init__(self, valor, taxa):
        # Chama o metodo construtor da classe Mãe
        super().__init__(valor)

        self.__taxa = taxa

    def calcular_valor(self):

        #
        return self.valor + (self.valor * self.__taxa / 100)


class PagamentoPix(Pagamento):

    def __init__(self, valor, desconto):

        super().__init__(valor)

        # Atributo privado que representa o desconto porcentual do Pix
        self.__desconto = desconto

    def calcular_valor(self):

        return self.valor - (self.valor * self.__desconto / 100)

class PagamentoBoleto(Pagamento):

    def __init__(self, valor, taxa_fixa):
        super().__init__(valor)

        self.__taxa_fixa = taxa_fixa

    def calcular_valor(self):

        return self.valor + self.__taxa_fixa


    # Lista que irá armazenar todos os pagamentos criados.
pagamentos = []

quantidade = int(input(" Quantos pagamentos deseja processar ? "))

# Laço para criar vários pagamentos:

for i in range(quantidade):

    # Nosso menu para escolher a forma de pagamento:
    print("\n1 - Cartão")
    print("2 - Pix")
    print("3 - Boleto")

    tipo = int(input("Escolha a forma de pagamento: "))

    valor = float(input("Digite o valor do boleto de pagamento: "))

    if tipo == 1:

        taxa = float(input("Digite a taxa do cartão: "))
        pagamento = PagamentoCartao(valor, taxa)

    elif tipo == 2:

        desconto =  float(input("Digite o desconto do  Pix: "))
        pagamento = PagamentoPix(valor, desconto)

    elif tipo == 3:

        taxa_fixa = float(input("Digite a taxa fixa do boleto: "))
        pagamento = PagamentoBoleto(valor, taxa_fixa)

    else:

        print("Forma de pagamento invalida! ")
        continue

    pagamentos.append(pagamento)


total_geral = 0 # Variável para somar todos os pagamentos


for pagamento in pagamentos:

    valor_final = pagamento.calcular_valor()

    print(f"Valor final: {valor_final}")

    total_geral += valor_final

print(f"\nTotal processado: {total_geral}")