def convert_to_int(string):
    try:
        return int(string)
    except ValueError:
        print("Peringatan: Input harus berupa angka, bukan teks.")
        return None

while True:
    umur = input("Masukkan umur kamu :")
    umur5tahunlagi = convert_to_int(umur)
    if umur5tahunlagi is not None:
        print(f"Umur kamu 5 tahun lagi adalah {umur5tahunlagi + 5}")
        break