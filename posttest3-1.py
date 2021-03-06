import time
import random
import os

harga_keju = 6000
harga_cokelat = 3500
nomor_pembayaran = random.randint(1000, 9999)
menu2 = "\n[8] Bayar & Keluar\n[9] Kembali ke Menu\n[0] Keluar\n"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def konfirmasi():
    select = input("Pilih menu [0-9]\t: ")
    if select == '8':
        print("\nNomor Pembayaran: {}\nMohon lakukan pembayaran segera.\nTerima kasih dan selamat menikmati~\n".format(nomor_pembayaran))
        time.sleep(1)
        exit(1)
    elif select == '9':
        pass
    elif select == '0':
        print("\nTerima kasih telah berkunjung ~ 👋😊")
        time.sleep(1)
        exit(1)
    else:
        print("Input salah.")
        konfirmasi()

while True:
    clear()
    print("""==================================
 Selamat Datang di Toko Kue Sule~
 UNTUK HARI INI PROMO HINGGA 15%!

Rasa         Sebanyak       Diskon
==================================
Keju             4-15          10% 
                16-25          15% 
Cokelat          5-20           7% 
                21-35          12% 
==================================
Menu:
[1] Kue Keju                Rp6000
[2] Kue Cokelat             Rp3500
[9] Tentang
[0] Keluar
==================================
""")
    pilihan = input("Pilih menu [0-9]\t: ")
    if pilihan == '1':
        while True:
            try:
                kuantitas_keju = int(input("Pesan sebanyak\t\t: "))
            except:
                print("Mohon gunakan angka dalam kuantitas pembelian.")
                time.sleep(1)
                pass
            else:
                if kuantitas_keju > 0 and kuantitas_keju < 4:
                    biaya_asli_keju = kuantitas_keju * harga_keju
                    print("\nHarga {} Kue Keju = Rp{}\nBeli lebih dari 3 untuk diskon 10%!".format(kuantitas_keju, biaya_asli_keju))
                    print(menu2)
                    konfirmasi()
                    break
                elif kuantitas_keju >= 4 and kuantitas_keju <= 15:
                    biaya_asli_keju = kuantitas_keju * harga_keju
                    diskon_keju = biaya_asli_keju * 0.10
                    promo_keju = biaya_asli_keju - int(diskon_keju)
                    hemat = biaya_asli_keju - promo_keju
                    print("\nHarga {} Kue Keju\t: Rp{}\nDiskon 10% menjadi\t: Rp{}\nAnda hemat sebesar\t: Rp{}\nBeli lebih dari 15 untuk diskon 15%!".format(kuantitas_keju, biaya_asli_keju, promo_keju, hemat))
                    print(menu2)
                    konfirmasi()
                    break
                elif kuantitas_keju >= 16 and kuantitas_keju <= 25:
                    biaya_asli_keju = kuantitas_keju * harga_keju
                    diskon_keju = biaya_asli_keju * 0.15
                    promo_keju = biaya_asli_keju - int(diskon_keju)
                    hemat = biaya_asli_keju - promo_keju
                    print("\nHarga {} Kue Keju\t: Rp{}\nDiskon 15% menjadi\t: Rp{}\nAnda hemat sebesar\t: Rp{}".format(kuantitas_keju, biaya_asli_keju, promo_keju, hemat))
                    print(menu2)
                    konfirmasi()
                    break
                elif kuantitas_keju > 25:
                    print("Mohon maaf, kami hanya menyediakan 25 Kue Keju perhari.")
                    time.sleep(1.5)
                elif kuantitas_keju <= 0:
                    print("Mohon gunakan angka yang benar.")
                    time.sleep(1.5)
    elif pilihan == '2':
        while True:
            try:
                kuantitas_cokelat = int(input("Pesan sebanyak\t\t: "))
            except:
                print("Mohon gunakan angka dalam kuantitas pembelian.")
                time.sleep(1)
                pass
            else:
                if kuantitas_cokelat > 0 and kuantitas_cokelat < 5:
                    biaya_asli_cokelat = kuantitas_cokelat * harga_cokelat
                    print("\nHarga {} Kue Cokelat = Rp{}\nBeli lebih dari 4 untuk diskon 7%!".format(kuantitas_cokelat, biaya_asli_cokelat))
                    print(menu2)
                    konfirmasi()
                    break
                elif kuantitas_cokelat >= 5 and kuantitas_cokelat <= 20:
                    biaya_asli_cokelat = kuantitas_cokelat * harga_cokelat
                    diskon_cokelat = biaya_asli_cokelat * 0.07
                    promo_cokelat = biaya_asli_cokelat - int(diskon_cokelat)
                    hemat = biaya_asli_cokelat - promo_cokelat
                    print("\nHarga {} Kue Cokelat\t: Rp{}\nDiskon 7% menjadi\t: Rp{}\nAnda hemat sebesar\t: Rp{}\nBeli lebih dari 20 untuk diskon 12%!".format(kuantitas_cokelat, biaya_asli_cokelat, promo_cokelat, hemat))
                    print(menu2)
                    konfirmasi()
                    break
                elif kuantitas_cokelat >= 21 and kuantitas_cokelat <= 35:
                    biaya_asli_cokelat = kuantitas_cokelat * harga_cokelat
                    diskon_cokelat = biaya_asli_cokelat * 0.12
                    promo_cokelat = biaya_asli_cokelat - int(diskon_cokelat)
                    hemat = biaya_asli_cokelat - promo_cokelat
                    print("\nHarga {} Kue Cokelat\t: Rp{}\nDiskon 12% menjadi\t: Rp{}\nAnda hemat sebesar\t: Rp{}".format(kuantitas_cokelat, biaya_asli_cokelat, promo_cokelat, hemat, nomor_pembayaran))
                    print(menu2)
                    konfirmasi()
                    break
                elif kuantitas_cokelat > 35:
                    print("Mohon maaf, kami hanya menyediakan 35 Kue Coklat perhari.")
                    time.sleep(1.5)
                elif kuantitas_cokelat <= 0:
                    print("Mohon gunakan angka yang benar.")
                    time.sleep(1.5)
    elif pilihan == '9':
        print("\nProgram ini dibuat oleh:\nFazri Rahmad Nor Gading (2009106031)\nInformatika A '20 - Universitas Mulawarman\n")
        konfir = input("Tekan Enter untuk kembali: ")
        pass
    elif pilihan == '0':
        print("\nTerima kasih telah berkunjung ~ 👋😊")
        time.sleep(1)
        exit(1)
    else:
        print("Input salah.")
        time.sleep(1)
        pass