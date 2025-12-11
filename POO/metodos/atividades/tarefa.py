class Tarefa:

    def __init__(self, descricao):
        self.descricao = descricao
        self.concluido = False

    def marcar_concluida(self):
        self.concluido = True
        print(f"Tarefa: {self.descricao} marcada como CONCLUÍDA")

tarefa_py = Tarefa("Aprender Métodos em Python")
tarefa_py.marcar_concluida()