class Alarme:
    def __init__(self, senha):
        self.senha = senha
        self.armado = False
        self.disparado = False

    def armar(self, senha_tentativa):
        if senha_tentativa == self.senha:
            self.armado = True
            print(" Sistema ARMADO. Segurança ativada.")
        else:
            print(" Senha incorreta. Permanece desarmado.")

    def disparar(self):
        if self.armado and not self.disparado:
            self.disparado = True
            print(" ALARME ATIVADO! POLÍCIA CHAMADA! ")
        elif not self.armado:
            print("Alarme não pode disparar, pois não está armado.")

    def desarmar(self, senha_tentativa):
        if senha_tentativa == self.senha:
            self.armado = False
            self.disparado = False
            print(" Sistema DESARMADO. Alarme silenciado.")
        else:
            print(" Senha incorreta. O alarme continua ativo.")


# TESTE:
casa_segura = Alarme(1234)
casa_segura.armar(9999)  # Incorreto
casa_segura.armar(1234)  # Correto (Armado = True)
casa_segura.disparar()  # (Disparado = True)
casa_segura.desarmar(9999)  # Incorreto
casa_segura.desarmar(1234)  # Correto (Armado/Disparado = False)