# Kode Produk: Kategori - Tahun - ID Unik
Kode_item = "Laptop-2026-X99"

# 1. Mengambil Kategori (Karakter indeks 0 sampai sebelum 6)
Kategori = Kode_item[0:6]
print("Kategori:", Kategori) #Output: Laptop

# 2. Mengambil Tahun (Bisa menggunakan indeks negatif dari belakang)
# -8 adalah angka '2' pada '2026', -4 adalah '-' sebelum 'X99'
tahun = Kode_item[-8:-4]
print("Tahun Rilis:", tahun) #Output: 2026

# 3. Mengambil ID Unik (Dari indeks 12 sampai habis)
id_unik = Kode_item[12:]
print("ID Unik:", id_unik) #Output: X99

# 4. Trik Pembalikan String (Menggunakan 'step' negatif)
teks_rahasia = "nothyp"
print("Dibalik menjadi:", teks_rahasia[::-1]) #Output: python