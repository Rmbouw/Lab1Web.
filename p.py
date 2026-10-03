# Input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Logika hitung salah (ditambah 1)
hasil_salah = angka1 + angka2 + 1

# Hilangkan koma desimal jika angkanya bulat
if hasil_salah.is_integer():
    hasil_salah = int(hasil_salah)

# Tampilkan hasil
print(f"Hasil: {hasil_salah}")