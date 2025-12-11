class Livros:

    def __init__(self, titulo_dado, autor_dado):
        self.titulo = titulo_dado
        self.autor = autor_dado

    def exibir_info(self):
        print(f"Livro Cadastrado: {self.titulo} - {self.autor}")

print("-"*40)
print(" Cadastro de novo livro (1/2) ")
print("-"*40)

titulo_a = input("Digite o Titulo do Livro A:")
autor_a = input("Digite o Autor do Livro A:")


livro_a = Livros(titulo_a, autor_a)

print("-"*40)
print(" Cadastro de novo livro (2/2) ")
print("-"*40)


titulo_b = input("Digite o Titulo do Livro B:")
autor_b = input("Digite o Autor do Livro B:")
livro_b = Livros(titulo_b, autor_b)

print("\n" + "-"*40)
print("Verificação final: o Poder do 'SELF'")
print("-"*40)

livro_a.exibir_info()
livro_b.exibir_info()

print("\n  --- Acessando atributos Diretamente---")
print(f"titulo no Objeto A: {livro_a.titulo}")
print(f"titulo no Objeto B: {livro_b.titulo}")