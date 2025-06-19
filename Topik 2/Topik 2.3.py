class Cashier:
    def __init__(self, items, prices):
        self.items = items
        self.prices = prices

    def calculate_total(self, selected_items):
        total = 0
        for item in selected_items:
            if item not in self.items:
                # Jika item tidak ada, langsung lempar ValueError
                raise ValueError(f"Maaf, item '{item}' tidak tersedia.")
            else:
                index = self.items.index(item)
                price = self.prices[index]
                total += price
        return total

# Daftar barang dan harga
items = ["apel", "pisang", "jeruk"]
prices = [2500, 1500, 3000]

cashier = Cashier(items, prices)

# Ulangi input sampai item valid
while True:
    selected_items = input("Masukkan item yang dibeli (pisahkan dengan koma): ").lower().split(",")
    selected_items = [item.strip() for item in selected_items]

    try:
        total_price = cashier.calculate_total(selected_items)
        print("Total belanja:", total_price)
        break
    except ValueError as e:
        print(e)
        print("Silakan input ulang.\n")