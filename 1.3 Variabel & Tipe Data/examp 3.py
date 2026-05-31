# Menggunakan tipe data dasar dalam satu scenario
nama_produk = "Logitech G Pro X"  # str
harga_asli = 1500000              # int
diskon = 0.15                     # float(15%)
apakah_ready = True               # bool
catatan_pembeli = None            # NoneType (artinya belum diisi)

# Menghitung harga setelah diskon
# Tips: hasil pembagian atau perkalian float otomatis menghasilkan float
harga_diskon = harga_asli * (1 - diskon)

print("Nama Produk:", nama_produk)
print("Harga setelah diskon:", harga_diskon)
print("Tipe harga_diskon:", type(harga_diskon))  # Akan menghasilkan <class 'float'>