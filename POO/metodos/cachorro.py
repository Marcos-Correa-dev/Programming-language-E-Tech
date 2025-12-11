class Cachorro:

    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    # Metodo: Comportamento/ação
    def latir(self):
        return f"{self.nome} o cachorroa🐶 está latindo: 'AU AU'"

    # Método: Comportamento que modifica o estado do objeto

    def fazer_aniversario(self):
        self.idade += 1 # Modifica o atributo 'idade'
        return f"Parabéns! {self.nome} agora tem {self.idade} anos. "

    # Metódo: Comportamento que usa múltiplos atributos
    def apresemtar(self):
        return f"Olá, eu sou {self.nome}. um(a) {self.raca} de {self.idade} anosa."

dog_a = Cachorro("Max", "Golden Retriever", 5)
dog_b = Cachorro("Luna", "Poodle", 2)

print(dog_a.apresemtar())
print(dog_a.latir())

print(dog_b.apresemtar())
print(dog_b.latir())

# Alterando o estado do Max através de um metódo
print(dog_a.fazer_aniversario())
print(dog_a.apresemtar()) # Verifica a idade atualizada (6 anos)