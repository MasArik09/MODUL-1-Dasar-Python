# Pendeklarasian variabel - langsung saja, tanpa tipe
nama = "Budi"           # str (string/teks)
umur = 20               # int (bilangan bulat)
tinggi = 170.5          # float (bilangan desimal)
lulus = True            # bool (True / False)
kosong = None           # NoneType (tidak ada nilai)

# Cek tipe data
print(type(nama))  # <class 'str'>
print(type(umur))  # <class 'int'>
print(type(lulus))  # <class 'bool'>

# Multi assignment
x = y = z = 0
a, b, c = 1, 2, 3