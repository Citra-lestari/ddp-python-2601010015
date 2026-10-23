# Program menghitung luas dan keliling persegi panjang
panjang = float(input("Masukkan panjang (M): "))
lebar = float(input("Masukkan lebar (M): "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas : {luas: } m2")
print(f"Keliling : {keliling: } m")

# Trace table:
# Langkah         | Panjang | Lebar | Luas | Keliling |
# Input           | 8       | 5     | -    | -        |
# Hitung luas     | 8       | 5     | 40   | -        |
# Hitung keliling | 8       | 5     | 40   | 26       |