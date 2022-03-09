#membuat garis
def garis():
    print("------------------------------")

#tampilan menu
print("----------HOTEL SMK JP ONE----------")
print("-- lama inap ------ superior ------- deluxe -------- premium --")
print("- 1 s.d 2 hari - 100.000/night - 150.000/night - 200.000/night -")
print("- 3 s.d 4 hari - 90.000/night  - 135.000/night - 180.000/night -")
print("- 5 harikeatas - 80.000/night  - 120.000/night - 160.000/night -")

#input data
nama = input("Masukan Nama Lengkap : ")
tipe_kamar = input("Masukan Tipe Kamar : ")
lama_inap = int(input("Masukan Lama Menginap : "))

#tipe superior
if tipe_kamar == "superior":
    if lama_inap <= 2:
        total_harga = 100000*lama_inap
    elif lama_inap <= 4:
        total_harga = 90000*lama_inap
    elif lama_inap == 5:
        total_harga = 80000*lama_inap
    else:
        total_harga = 80000*lama_inap+80000*lama_inap/2
        pegawai = print("Komisi pegawai ditambahkan 50% dari harga normal diatas 5 hari")


#tipe deluxe
elif tipe_kamar == "deluxe":
    if lama_inap <= 2:
        total_harga = 150000*lama_inap
    elif lama_inap <= 4:
        total_harga = 135000*lama_inap
    elif lama_inap == 5:
        total_harga = 120000*lama_inap
    else:
        total_harga = 120000*lama_inap+120000*lama_inap/2
        pegawai = print("Komisi pegawai ditambahkan 50% dari harga normal diatas 5 hari")


#tipe premium
elif tipe_kamar == "premium":
    if lama_inap <= 2:
        total_harga = 200000*lama_inap
    elif lama_inap <= 4:
        total_harga = 180000*lama_inap
    elif lama_inap == 5:
        total_harga = 160000*lama_inap
    else:
        total_harga = 160000*lama_inap+160000*lama_inap/2
        pegawai = print("Komisi pegawai ditambahkan 50% dari harga normal di atas 5 hari")


#total harga menginap
garis()
print(" Nama Lengkap : ", (nama))
print(" Tipe Kamar yang Dipilih : ", (tipe_kamar))
print(" Lama Menginap : ", (lama_inap)," Hari")
print(" Total Harga Yang Dibayar : RP. ", round(total_harga))
