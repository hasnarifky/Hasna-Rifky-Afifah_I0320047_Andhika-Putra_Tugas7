#program menggunakan fungsi string

judul = input("Judul : ")
kalimat1 = input("Kalimat ke-1 : ")
kalimat2 = input("Kalimat ke-2 : ")
kalimat3 = input("Kalimat ke-3 : ")
n = len(kalimat1) + len(kalimat2) + len(kalimat3)

print("\nKoreksi tanda baca titik di akhir kalimat")
print(" - True : sudah benar penulisan tanda baca titik.")
print(" - False : Anda belum memasukkan tanda baca titik.")
print("Tanda baca pada kalimat pertama : ", kalimat1.endswith("."))
print("Tanda baca pada kalimat kedua : ", kalimat2.endswith("."))
print("Tanda baca pada kalimat ketiga : ", kalimat3.endswith("."))

print(" ")
print("HASIL KOREKSI")
print(" ")

judul2 = judul.upper()
judul3 = judul2.center(n, ' ')
print(judul3)
print(" ")

k1 = kalimat1.capitalize()
k2 = kalimat2.capitalize()
k3 = kalimat3.capitalize()
print("%s. %s. %s. " % (k1, k2, k3))
print(" ")
