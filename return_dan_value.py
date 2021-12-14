def tambah(angka1, angka2):
    total = angka1 + angka2
    print(f'Angka {angka1} + Angka {angka2} = {total}')
    return total    # jika tidak di return hasilnya adalah none


def kali(angka1, angka2):
    total = angka1 * angka2
    print(f'Angka {angka1} x Angka {angka2} = {total}')
    return total


# output ada 3
b = kali(3, tambah(4, 2))   # fungsi tambah dieksekusi terlebih dahulu
print(b)

