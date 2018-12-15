import math
def menu():
                print "\033[93m"
		print "Menu Pilihan"
                print "1. Luas Segitiga"
                print "2. Luas Lingkaran"
                print "3. Luas Trapesium"
                print "4. Luas Jajargenjang"
                print "5. Luas Bola"
                print "6. Luas Kerucut"
		print "0. Keluar"

def segitiga () :
                t = input("Masukkan tinggi segitiga : ")
                a = input("Masukkan alas segitiga : ")
                l = a * t * 1/2
                print (" Jadi luas segitiga adalah : "), l
                print ("Terima Kasih Telah Menggunakan Tools Kami:)")
		print

def lingkaran () :
                r = input("Masukkan jari - jari lingkaran : ")
                l = 3.14 * r * r
                print (" Jadi luas lingkaran adalah : "), l
                print ("Terima Kasih Telah Menggunakan Tools Kami:)")
		print

def trapesium () :
                t = input("Masukkan tinggi : ")
                j = input("Masukkan jumlah sisi sejajar : ")
                l = t * j / 2
                print (" Jadi luas trapesium adalah : "), l
                print ("Terima Kasih Telah Menggunakan Tools Kami:)")
		print

def jajargenjang () :
                t = input("Masukkan tinggi segitiga : ")
                a = input("Masukkan alas segitiga : ")
                l = a * t
                print (" Jadi luas jajargenjang adalah : "), l
                print ("Terima Kasih Telah Menggunakan Tools Kami:)")
		print

def bola () :
                r = input("Masukkan jari - jari : ")
                l = 4 * 3.14 * r * r
                print (" Jadi luas bola adalah : "), l
                print ("Terima Kasih Telah Menggunakan Tools Kami:)")
		print

def kerucut () :
                t = input("Masukkan tinggi segitiganya : ")
                r = input("Masukkan jari - jari alasnya : ")
                l = ( 3.14 *r ) * ( t * r )
                print (" Jadi luas kerucut adalah : "), l
                print ("Terima Kasih Telah Menggunakan Tools Kami:)")
		print
def keluar():
	    print "TERIMA KASIH TELAH MAMPIR"
	    print
	    exit()
#Program Utama
print
print "\033[94mSELAMAT DATANG DI PROGRAM MENGHITUNG LUAS"
print "------------------------------------------"
pilihan = 'y'
while (pilihan != 't'):
	menu()
	pilih = input("Masukkan pilihan : ")

	if pilih == 1:
        	        segitiga()
	elif pilih == 2:
        	        lingkaran()
	elif pilih == 3:
        	        trapesium()
	elif pilih == 4:
        	        jajargenjang()
	elif pilih == 5:
        	        bola()
	elif pilih == 6:
        	        kerucut()
	elif pilih == 0:
			keluar()
	else :
        	        print ("MASUKAN YANG BENER!!!")
	pilihan = raw_input("Ulangi Lagi? (y/t) ")
	continue
