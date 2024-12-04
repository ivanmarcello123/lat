x = [[1, 3, 4], [7, 3, 15], [15, 2, 5], [6, 8, 4]]
y = []

# Menghitung transpose
for i in range(len(x[0])):  # Iterasi untuk setiap kolom di x
    new_row = []  # Membuat baris baru untuk y
    for j in range(len(x)):  # Iterasi untuk setiap baris di x
        new_row.append(x[j][i])  # Menambahkan elemen dari x ke baris baru
    y.append(new_row)  # Menambahkan baris baru ke matriks y

# Menampilkan hasil
print("Matriks Transpose:")
for row in y:
    print(row)