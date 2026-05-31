teks = "Halo dunia"

# Slicing 
print(teks[0])      # H
print(teks[-1])     # a dari belakang
print(teks[0:4])   # Halo
print(teks[5:])    # dunia

# Method string
print(teks.upper())     # HALO DUNIA
print(teks.lower())     # halo dunia
print(teks.replace("Halo", "Selamat"))  # Selamat dunia
print(len(teks))        # 10

# f-string (cara modern format string)
nama = "Andi"
umur = 22
print(f"Nama saya {nama}, umur  {umur} tahun")