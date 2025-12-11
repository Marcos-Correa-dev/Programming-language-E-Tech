class PlayerMusical:
    def __init__(self):
        self.volume = 50
        self.tocando = False

    def play(self):
        if not self.tocando:
            self.tocando = True
            print("▶ Música iniciada.")

    def pause(self):
        if self.tocando:
            self.tocando = False
            print(" Música pausada.")

    def aumentar_volume(self, passos):
        self.volume += passos
        if self.volume > 100:
            self.volume = 100  # Garante que não ultrapasse 100
            print(f" Volume no máximo (100).")
        else:
            print(f" Volume ajustado para {self.volume}.")


# TESTE:
meu_player = PlayerMusical()
meu_player.play()
meu_player.aumentar_volume(60)  # Tenta ir para 110, mas para em 100
meu_player.pause()
meu_player.aumentar_volume(5)