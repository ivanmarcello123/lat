# Daftar produk di toko online TechMart
produk = ['smartphone','laptop', 'smartwatch', 'headphone', 'kamera', 'keyboard', 'mouse', 'printer', 'monitor', 'speaker']
print("(1)mengubah semua data produk jadi huruf kecil")
# Mengubah semua nama produk menjadi huruf kecil menggunakan list comprehension
produk_kecil = [p.lower() for p in produk]

# Menampilkan hasil
print("Daftar produk dengan huruf kecil:")
for p in produk_kecil:
    print(p)



# Menghitung jumlah produk
jumlah_produk = len(produk)

# Menampilkan hasil
print(f"(2)Jumlah produk yang tersedia: {jumlah_produk}")


# Meminta input produk dari pengguna
print("(3)cari produk disini:")
produk_cek = input("Masukkan nama produk yang ingin diperiksa: ").lower()

# Memeriksa apakah produk ada dalam daftar
if produk_cek in produk:
    print(f"{produk_cek} ada dalam daftar produk.")
else:
    print(f"{produk_cek} tidak ada dalam daftar produk.")


print("(4)Produk yang dimulai dengan huruf 's':")
for p in produk:
    if p.lower().startswith('s'):
        print(p)


print("(5)menggabungkan semua data:")
hasil='|'.join(produk)
print(hasil)
