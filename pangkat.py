'''
print pertama melakukan itersi sebanyak 2 kali
print kedua melakukan itersi sebanyak 3 kali
'''

def pangkat(angka, pangkatnya=2):
    hasil = 1
    for i in range(0, pangkatnya):
        hasil = hasil * angka
    return hasil


print(pangkat(3)) # 9
print(pangkat(3, 3)) # 27
