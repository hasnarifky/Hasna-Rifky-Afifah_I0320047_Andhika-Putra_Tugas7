#program menggunakan fungsi numerik

print("Selamat datang di program")
nama = input("Nama : ")
import math
print("Masukkan nilai (skala 1-10, dapat berupa desimal. Contoh : 8.9)")
a = float(input("Nilai 1 : "))
b = float(input("Nilai 2 : "))
c = float(input("Nilai 3 : "))
d = float(input("Nilai 4 : "))
e = float(input("Nilai 5 : "))

a1 = math.fabs(a)
b1 = math.fabs(b)
c1 = math.fabs(c)
d1 = math.fabs(d)
e1 = math.fabs(e)

nilai_max = max(a,b,c,d,e)
nilai_min = min(a,b,c,d,e)

jumlah = a1 + b1 + c1 + d1 + e1
rata = jumlah/5
rata_bulat = math.ceil(rata)

print('-'*17)
print("HASIL PERHITUNGAN")
print('-'*17)

print("Nama : ", nama)
print("Rata-rata nilai adalah", rata, "jika dibulatkan menjadi", rata_bulat)
print("Nilai tertinggi yaitu", nilai_max)
print("Nilai terendah yaitu", nilai_min)
