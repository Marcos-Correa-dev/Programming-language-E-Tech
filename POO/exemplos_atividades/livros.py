class Livro:
    def __init__(self, titulo, autor):
        # 'self' garante que 'titulo' seja um atributo deste Livro específico
        self.titulo = titulo
        self.autor = autor

# Criação do Livro A
livro_a = Livro("Duna", "Frank Herbert")
# Dentro do __init__, 'self' se refere a 'livro_a'

# Criação do Livro B
livro_b = Livro("1984", "George Orwell")
# Dentro do __init__, 'self' se refere a 'livro_b'

# Eles têm o mesmo atributo 'titulo', mas com valores diferentes,
# pois 'self' apontou para instâncias diferentes.
print(livro_a.titulo) # Saída: Duna
print(livro_b.titulo) # Saída: 1984