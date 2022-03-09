def garis():
    print("----------------------------------")

#fungsi bubble sort ascending (dari kecil ke besar)
def sort_asc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range(n-i-1):
            #membandingkan masing" elemen ke kanan
            if array[j] > array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
        return array

#fungsi bubble sort diescending (dari besar ke kecil)
def sort_desc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range(n-i-1):
            #membandingkan masing" elemen ke kanan
            if array[j] < array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
        return array

#fungsi rata rata
def rata_rata(angka):
    return sum(angka)/len(angka)

#input nilai
garis()
print("Masukkan Nama Lengkap & Kelas Kalian")
nama_lengkap = input("Nama Lengkap : ")
kelas = input("Kelas : ")

print("Masukkan Nilai Kalian")
nilai_a = int(input("Nilai Bahasa Inggris : "))
nilai_b = int(input("Nilai Bahasa Indonesia : "))
nilai_c = int(input("Nilai Bahasa Mandarin : "))
nilai_d = int(input("Nilai Bahasa Jepang : "))
nilai_e = int(input("Nilai Bahasa Sunda : "))
nilai_f = int(input("Nilai Bahasa Jawa : "))
nilai_g = int(input("Nilai Bahasa Rusia : "))
nilai_h = int(input("Nilai Bahasa Ilmu Pesatiran : "))
nilai_i = int(input("Nilai Bahasa Ilmu Pesarkas Handal : "))
nilai_j = int(input("Nilai Bahasa Perancis : "))
angka = [nilai_a, nilai_b, nilai_c, nilai_d, nilai_e, nilai_f, nilai_g, nilai_h, nilai_i, nilai_j]
garis()
print()

#nilai akhir
print("HASIL AKHIR----")
print("Urutan Angka ascending : ", (sort_asc(angka)))
print("Urutan Angka descending : ", (sort_desc(angka)))

#angka terbesar
print("Angka Terbesar : ", max(angka))

#angka terkecil
print("Angka Terkecil : ", min(angka))

#rata rata
print("Rata ratanya : ", round(rata_rata(angka),2))
