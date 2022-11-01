import time;
localtime = time.asctime( time.localtime(time.time()) )

from os import access, name
from typing import Optional

def login(name,idpelanggan):
    sukses = False
    file = open("logindatabase.txt", "r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if (a==name and b==idpelanggan):
            sukses = True
            break
    file.close()
    if(sukses):
        print("-"*40)
        print("     login berhasil, Silahkan masuk")
        print("-"*40)
    else:
        print("-"*50)
        print("Anda belum terdaftar, silahkan register")
        print("-"*50)
        begin()
        access(option)

def register(name,idpelanggan):
    file = open("logindatabase.txt", "a")
    file.write("\n"+name+","+idpelanggan)

def access(option):
    global name
    if(option == "login"):
        name = input("Masukkan Nama : ")
        idpelanggan = input("Masukkan IdPelanggan : ")
        login(name,idpelanggan)
    else:
        print(" | Masukkan Nama dan IdPelanggan anda yang baru | ")
        name = input("Masukkan Nama : ")
        idpelanggan = input("Masukkan IdPelanggan : ")
        register(name,idpelanggan)
        print(" | Register anda berhasil, Silahkan masuk | ")

def begin():
    global option
    print("="*45)
    print(" | Selamat Datang di Laundry Mahasiswa | ")
    print("Ketik 'login' jika anda sudah punya akun")
    print("Ketik 'reg' jika anda belum punya akun")
    print("-"*45)
    option = input("Silahkan Masukkan (login/reg) : ")
    if(option!="login" and option!="reg"):
        begin()
begin()
access(option)


nama = str(input('Nama Anda: '))
alamat = input('Alamat Anda: ')
NoTelp = int(input('Masukkan NoTelf: '))
Keterangan = input('Masukkan Keterangan: ')

total = []

def menu():
    print("---------------Menu Laundry Mahasiswa----------------")
    print(" No|        Jenis         | Lama Pengerjaan | Biaya  ")
    print("-----------------------------------------------------")
    print(" 1 | Cuci Komplit Reguler | 2-3 Hari        | 7000   ")
    print(" 2 | Cuci Komplit Kilat   |   1 Hari        | 12000  ")
    print(" 3 | Cuci Komplit Express |   8  jam        | 7000   ")
    print(" 4 | Cuci Kering Reguler  | 2-3 Hari        | 6000   ")
    print(" 5 | Cuci Kering Kilat    |   1 Hari        | 9000   ")
    print(" 6 | Cuci Kering Express  |   8 jam         | 10000  ")
    print(" 7 | Setrika Reguler      |  2-3 Hari       | 6000   ")
    print(" 8 | Setrika Kilat        |  1 Hari         | 9000   ")
    print(" 9 | Setrika Reguler      |  8 jam          | 10000  ")
    print(" 10| Karpet                                 | 15000  ")
    print(" 11| Jas                                    | 15000  ")
    print(" 12| Bantal Guling kecil/sedang             | 9000   ")
    print(" 13| Bantal/Guling besar                    | 12000  ")
    print(" 14| Boneka kecil/sedang                    | 7000   ")
    print(" 15| Boneka besar                           | 12000  ")
    print(" 16| Celana panjang biasa/jeans             | 7000   ")
    print(" 17| Skirt & Blouse                         | 5000   ")
    print(" 18| Celana pendek biasa/jeans              | 5000   ")
    print(" 19| Kemeja/kaus lengan panjang             | 8000   ")
    print(" 20| Kemeja/kaus lengan pendek              | 5000   ")
    print(" 21| Jaket non kulit                        | 10000  ")
    pilih = int(input("Masukkan Pilihan: "))
    if pilih == 1:
        berat_jumlah = float(input("Berat Pakaian(kg) :"))
        total1 = berat_jumlah*7000
        total.append(total1)
        print(berat_jumlah,"Cuci Komplit Reguler_2-3 Hari", total)
        tanya()
    elif pilih == 2:
        berat_jumlah = float(input("Berat Pakaian(kg) :"))
        total2 = berat_jumlah*12000
        total.append(total2)
        print(berat_jumlah,"Cuci Komplit Kilat_1 Hari", total)
        tanya()
    elif pilih == 3:
        berat_jumlah = float(input("Berat Pakaian(kg) :"))
        total3 = berat_jumlah*15000
        total.append(total3)
        print(berat_jumlah,"Cuci Komplit Express_8 jam", total)
        tanya()
    elif pilih == 4:
        berat_jumlah = float(input("Berat Pakaian(kg) :"))
        total4 = berat_jumlah*6000
        total.append(total4)
        print(berat_jumlah,"Cuci Kering Reguler_2-3 Hari", total)
        tanya()
    elif pilih == 5:
        berat_jumlah = float(input("Berat Pakaian(kg) :"))
        total5 = berat_jumlah*9000
        total.append(total5)
        print(berat_jumlah,"Cuci Kering Kilat_1 Hari", total)
        tanya()
    elif pilih == 6:
        berat_jumlah = float(input("Berat Pakaian(kg) :"))
        total6 = berat_jumlah*10000
        total.append(total6)
        print(berat_jumlah,"Cuci Kering Express_8 jam", total)
        tanya()
    elif pilih == 7:
        berat_jumlah = float(input("Berat Pakaian(kg) :"))
        total7 = berat_jumlah*6000
        total.append(total7)
        print(berat_jumlah,"Setrika Reguler_2-3 Hari", total)
        tanya()
    elif pilih == 8:
        berat_jumlah = float(input("Berat Pakaian(kg) :"))
        total8 = berat_jumlah*9000
        total.append(total8)
        print(berat_jumlah,"Setrika Kilat_1 Hari", total)
        tanya()
    elif pilih == 9:
        berat_jumlah = float(input("Berat Pakaian(kg) :"))
        total9 = berat_jumlah*10000
        total.append(total9)
        print(berat_jumlah,"Setrika Express_8 jam", total)
        tanya()
    elif pilih == 10:
        berat_jumlah = int(input("Jumlah(Satuan)  :"))
        total10 = berat_jumlah*15000
        total.append(total10)
        print(berat_jumlah,"karpet", total)
        tanya()
    elif pilih == 11:
        berat_jumlah = int(input("Jumlah(Satuan) :"))
        total11 = berat_jumlah*15000
        total.append(total11)
        print(berat_jumlah,"Jas", total)
        tanya()
    elif pilih == 12:
        berat_jumlah = int(input("Jumlah(Satuan) :"))
        total12 = berat_jumlah*9000
        total.append(total12)
        print(berat_jumlah,"Bantal Guling kecil/sedang", total)
        tanya()
    elif pilih == 13:
        berat_jumlah = int(input("Jumlah(Satuan) :"))
        total13 = berat_jumlah*12000
        total.append(total13)
        print(berat_jumlah,"Bantal Guling Besar", total)
        tanya()
    elif pilih == 14:
        berat_jumlah = int(input("Jumlah(Satuan) :"))
        total14 = berat_jumlah*7000
        total.append(total14)
        print(berat_jumlah,"Boneka kecil/sedang", total)
        tanya()
    elif pilih == 15:
        berat_jumlah = int(input("Jumlah(Satuan) :"))
        total15 = berat_jumlah*12000
        total.append(total15)
        print(berat_jumlah,"Boneka Besar", total)
        tanya()
    elif pilih == 16:
        berat_jumlah = int(input("Jumlah(Satuan) :"))
        total16 = berat_jumlah*7000
        total.append(total16)
        print(berat_jumlah,"Blouse/Celana panjang biasa/jeans", total)
        tanya()     
    elif pilih == 17:
        berat_jumlah = int(input("Jumlah(Satuan) :"))
        total17 = berat_jumlah*5000
        total.append(total17)
        print(berat_jumlah,"Skirt & Blouse", total)
        tanya()
    elif pilih == 18:
        berat_jumlah = int(input("Jumlah(Satuan) :"))
        total18 = berat_jumlah*5000
        total.append(total18)
        print(berat_jumlah,"Celana pendek biasa/jeans", total)
        tanya()
    elif pilih == 19:
        berat_jumlah = int(input("Jumlah(Satuan) :"))
        total19 = berat_jumlah*8000
        total.append(total19)
        print(berat_jumlah,"Kemeja/kaus lengan panjang", total)
        tanya()
    elif pilih == 20:
        berat_jumlah = int(input("Jumlah(Satuan) :"))
        total20 = berat_jumlah*5000
        total.append(total20)
        print(berat_jumlah,"Kemeja/kaus lengan pendek", total)
        tanya()
    elif pilih == 21:
        berat_jumlah = int(input("Jumlah(Satuan) :"))
        total21 = berat_jumlah*10000
        total.append(total21)
        print(berat_jumlah,"Jaket non kulit", total)
        tanya()
    else: 
        print("Pilihan tidak tersedia")
        menu()
      

def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah pesanan? [y/t] : ")
    print("---------------------------------")
    if tanya == "y" or tanya == "Y":
        menu()
    elif tanya == "t" or tanya == "T":
        akhir()
    else:
        print("Pilihan tidak tersedia")


def akhir():
    for harga in total:
        print("SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 30000:
            diskon = a * 5/100
        elif a > 40000:
            diskon = a * 10/100
        elif a > 50000:
            diskon = a * 15/100
        elif a > 70000:
            diskon = a * 20/100
        else:
            diskon = 0
        print("Potongan Harga   : Rp.", diskon)
        totalakhir = a - diskon
        uang=int(input("Uang Tunai Pembeli: Rp."))
        kembalian=(uang-totalakhir)
        print("Kembalian : Rp.",kembalian)
        print(" ")
        print("------------STRUK LAUNDRY MAHASISWA-----------")
        print("----------HP/WA Laundry 085155243242----------")
        print("==============================================")
        print("Nama Anda             : ", nama)
        print("NoTelp                : ", NoTelp)
        print("Alamat Anda           : ", alamat)
        print("Keterangan Laundry    : ", Keterangan)
        print("Tagihan               : Rp.", totalakhir)
        print("Uang                  : Rp.", uang)
        print("Kembalian             : Rp.", kembalian)
        print("-----------------Terima Kasih-----------------")
        print("------------Telah Mempercayai Kami------------")
        print("==========",localtime,"==========")

menu() 