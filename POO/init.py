

class Livro:
    
    # o Montador da Fábrica (Construtor)
    def __init__(self, titulo_dado, autor_dado):
        # A magia acontece aqui, os atributos são iniciados
        self.titulo = titulo_dado
        self.autor = autor_dado
        
livro_1 = Livro("Interistellar", "Guilherme")
print(livro_1.titulo)
        
    