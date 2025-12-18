class Pessoa:
    def __init__(self, nome):
        # Atributo PROTEGIDO (convenção)
        self._nome = nome


pessoa = Pessoa("Carlos")

# Funciona, mas NÃO é recomendado
print(pessoa._nome)

# Alteração direta também funciona
pessoa._nome = "João"
print(pessoa._nome)
