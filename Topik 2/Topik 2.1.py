def calculate_average(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError("Masukkan list, bukan string atau integer.")
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError as e:
        print("Peringatan:", e)
    except:
        print("Peringatan: Terjadi kesalahan.")

result = calculate_average("huruf text")  # Menguji error
print(result)

result = calculate_average([5, 5, 7, 8])  # Contoh input benar
print(result)