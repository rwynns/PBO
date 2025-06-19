class Handphone:
    def __init__(self, kamera, layar, bateria, merk):
        self.__kamera = kamera
        self.__layar = layar
        self.bateria = bateria
        self.merk = merk
        self.status = False
        self.level_baterai = 50

    # Getter dan Setter untuk __kamera
    def get_kamera(self):
        return self.__kamera

    def set_kamera(self, kamera):
        self.__kamera = kamera

    # Getter dan Setter untuk __layar
    def get_layar(self):
        return self.__layar

    def set_layar(self, layar):
        self.__layar = layar

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


# Objek awal
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

# Objek baru dan akses getter-setter
hp3 = Handphone("108MP", "6.5 inch", "6000mAh", "Xiaomi")
print("\n=== Objek hp3 ===")
print("Kamera sebelum diubah:", hp3.get_kamera())
print("Layar sebelum diubah:", hp3.get_layar())

hp3.set_kamera("200MP")
hp3.set_layar("6.8 inch")

print("Kamera setelah diubah:", hp3.get_kamera())
print("Layar setelah diubah:", hp3.get_layar())
