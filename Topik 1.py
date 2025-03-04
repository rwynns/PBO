class Handphone:
    def __init__(self, kamera, layar, bateria, merk):
        self.kamera = kamera
        self.layar = layar
        self.bateria = bateria
        self.merk = merk
        self.status = False
        self.level_baterai = 50

    def menyala(self):
        self.status = True
        return f"{self.merk} telah menyala"

    def mati(self):
        self.status = False
        return f"{self.merk} telah dimatikan"

    def isi_daya(self):
        self.level_baterai += 25
        self.level_baterai = min(self.level_baterai, 100)
        return f"Mengisi daya {self.merk}. Level baterai sekarang: {self.level_baterai}%"

    def menelfon(self):
        self.level_baterai -= 5
        return f"Melakukan panggilan menggunakan {self.merk}"

    def cek_baterai(self):
        return f"Level baterai {self.merk}: {self.level_baterai}%"

hp1 = Handphone("48MP", "6.1 inch", "5000mAh", "Samsung")
hp2 = Handphone("12MP", "6.7 inch", "4500mAh", "iPhone")

print(hp1.menyala())
print(hp1.cek_baterai())
print(hp1.menelfon())
print(hp1.isi_daya())
print(hp1.mati())

print(hp2.menyala())
print(hp2.cek_baterai())
print(hp2.menelfon())
print(hp2.cek_baterai())
print(hp2.isi_daya())
print(hp2.mati())