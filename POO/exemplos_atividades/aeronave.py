class Aeronave:

    espaco_aereo = "Controlado"
    total_aeronaves = 0

    def __init__(self, prefixo, companhia):

        Aeronave.total_aeronaves += 1

        self.prefixo = prefixo
        self.companhia = companhia
        self.altitude = 0


aeronave1 = Aeronave("PR-ABC", "Latam")
aeronave2 = Aeronave("GOL-456", "GOL")
aeronave3 = Aeronave("AZUL-999","AZUL")

print(f"Aeronave1: Prefixo: {aeronave1.prefixo} "
      f"| Altitude: {aeronave1.altitude} ")
print(f"Aeronave2: Prefixo: {aeronave2.prefixo} "
      f"| Altitude: {aeronave2.altitude}")
print(f"Aeronave 3: Prefixo: {aeronave3.prefixo} "
      f"| Altitude: {aeronave3.altitude}")
print(f"Total Aeronaves: {Aeronave.total_aeronaves}")