#!/usr/bin/python
import os
import httplib
import json
import sys
import time
from py_compile import compile as c
c('sederhana.py')

os.system('clear')

def menu():
		print "\033[91m"
                print "======================"
		print "Created by KANG NEWBIE"
		print "======================"
	       	print "\033[93mMenu Pilihan"
                print "1. Bio data"
                print "2. Tahun Kabisat"
		print "3. Nembak Cewek"
		print "4. Ternak LELE"
		print "5. Menghitung Saldo"
		print "6. Perkiraan Cuaca"
		print "7. Mencari Bilanga Prima"
		print "8. Membuat List Pegawai"
		print "9. Kuis Sosial Media"
		print "10. "
		print "0. KELUAR"

print
print ("\033[1;32mMasukan UserName&Password")
print ("\033[1;31;1mKalo Gak Tau Lihat Aja Scriptnya")
username = 'admin'
password = 'root'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("username : ")
        if uname == username:
                pwd = raw_input("password : ")

                if pwd == password:
                        print"\n\033[1;92m------------------------------------------",
			os.system('clear')
                else:
                        print "\n\033[1;36mSorry Invalid password !!!\033[00m"
                        print "Back Login\n"
                        restart()

        else:
                print "\n\033[1;36mSorry Invalid Username !!!\033[00m"
                print "Back Login\n"
                restart()

try:
        main()
except KeyboardInterrupt:
        os.system('clear')
        restart()

def biodata () :
	        print
		print "\033[94mSELAMAT DATANG DI PROGRAM BIODATA"
		print "\033[92m========================================================"
		print "\033[91m*KETIKAN DENGAN HURUF KAPITAL SAJA!"
		print "*tolong isi dengan baik dan benar semua data-data anda!"
		print "*jika anda mengalami kesulitan bertanyalah."
		print
		nama_lengkap = raw_input("\033[93mNama Lengkap: ")
		umur = raw_input("Umur: ")
		jenis_kelamin = raw_input("Jenis Kelamin: ")
		tempat_tanggal_lahir = raw_input("Tempat/tanggal lahir: ")
		alamat = raw_input("Alamat: ")
		agama = raw_input("Agama: ")
		tinggi_badan = raw_input("Tinggi badan: ")
		riwayat_penyakit = raw_input("Riwayat penyakit: ")
		hobi = raw_input("Hobi: ")
		sekolah = raw_input("Sekolah: ")

		teks = "\nNama Lengkap: {}\nUmur: {}\nJenis Kelamin: {}\nTempat/tanggal lahir: {}\nAlamat: {}\nAgama: {}\nTinggi badan: {}\nRiwayat penyakit: {}\nHobi: {}\nSekolah: {}\n-----------------".format(nama_lengkap, umur, jenis_kelamin, tempat_tanggal_lahir, alamat, agama, tinggi_badan, riwayat_penyakit, hobi, sekolah)
		file_bio = open("biodata.txt", "a")
		file_bio.write(teks)
		file_bio.close()
		print "\033[91mNOTE: semua data anda telah dimasukan ke file 'biodata.txt'.\n terima kasih :)"
		print

def tahunkabisat () :
	tahun = input("\033[92mInput tahun: ")

	if (tahun % 4) == 0:
	    if (tahun % 100) == 0:
        	if (tahun % 400) == 0:
	            print "-Tahun Tersebut Tahun Kabisat"
		    print
        	else:
	            print "-Tahun Tersebut Bukan Tahun Kabisat"
		    print
	    else:
        	print "-Tahun Tersebut Tahun Kabisat"
		print
	else:
	    print "-Tahun Tersebut Bukan Tahun Kabisat"
	    print

def nembakcewek ():
	def utama():
	    print "\033[92mMaukah ente menjadi istriku ?"
	    print "1 = Mau"
	    print "2 = Tidak Mau"
	    dipilih = raw_input("Pilih Nomor ( 1 / 2 ) : ")
	    if dipilih == "1":
	        print '"Aku berjanji akan cinta sampai mati sama kamu :* "'
	    elif dipilih == "2":
	        print '"Yahh jomblo lagi deh"'
	    else :
	        print "Pilihannya Cuma 1 Sama 2 Doang tong -_- "
	    ulangi()
	def ulangi():
	    dicobalagi = raw_input("Coba lagi ? [Y/T] : ")
	    if dicobalagi.lower() == "y":
        	utama()
	    elif dicobalagi.lower() == "t":
        	sys.exit("Dadah :)")
	    else :
        	print "Pilihannya Cuma Y dan T Doang tong -_- "
	        ulangi()
	utama()

def lele():
	print
	nama = raw_input("Siapa nama mu? ")
	jumlah_lele = int(input("Hai " + nama + " Berapa jumlah ikan lele yang kamu punya di kolam? "))
	print "Ikan lele mu di kolam :", jumlah_lele, "ekor"
	kasih_makan = int(input("Berapa kali Anda memberi pakan setiap harinya? "))

# Kondisi
	if kasih_makan == 2:
		print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
		print "Anda mengatur jadwal pakan yang tepat."
		print
	elif kasih_makan < 2:
		print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
		print "Anda mengatur jadwal pakan yang kurang tepat."
		print
	elif kasih_makan > 2:
		print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
		print "Anda memberikan pakan terlalu berlebihan."
		print
	elif kasih_makan == 0:
		print "Jadwal pakan Anda :", kasih_makan, "kali perhari."
		print "Maaf ikan lele Anda mati."
		print

def saldo ():
	print ("")
	print ("\033[92m------ PROGRAM PYTHON UNTUK MENGHITUNG SALDO ------")
	print ("")
	print ("by : KANG NEWBIE")
	print ("")

	tabungan = int(input("Masukkan jumlah tabungan :"))
	lama = int(input("Masukkan jumlah lama menabung (bulan) :"))

	if tabungan < 1000000 :
	 sukuBunga = 0.03
	 saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
	 print("")
	 print("Karena tabungan anda dibawah 1.000.000,\nbunga yang anda dapatkan 3%")
	 print("Saldo anda selama " + str (lama) + " bulan, adalah " +str (saldoAkhir))
	 print("")

	elif tabungan > 1000000 :
	 sukuBunga = 0.04
	 saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
	 print("")
	 print("Karena tabungan anda diatas 1.000.000,\nbunga yang anda dapatkan 4%")
	 print("Saldo anda selama " + str (lama) + " bulan, adalah " +str (saldoAkhir))
	 print("")

def cuaca():
	print
	kota= raw_input("\033[92mMasukkan Nama Kota : ")
	conn = httplib.HTTPSConnection("api.openweathermap.org")
	conn.request("GET", "/data/2.5/forecast?q="+kota.lower()+",id&mode=json&appid=503186110e24edea8f99643135fd77cc")

	res = conn.getresponse()
	data = json.loads(res.read())
	for a in range (len(data['list'])):
	    print "==============================================="
	    print "Tanggal",data['list'][a]['dt_txt']

	    for b in range(len(data['list'][a]['weather'])):
	        print "Nama kota ", kota
	        print "Cuaca",data['list'][a]['weather'][b]['main']
	        print  "Suhu ",int(data['list'][a]['main']['temp'])-273
	        print "Kecepatan angin ",data['list'][a]['wind']['speed']
	    print "==============================================="

def prima():
	def is_prime(num):
		if num < 2:
			return False
		for prime in range(2, num):
			if num % prime == 0:
				return False
		return True

	def find_primes(max_num):
		primes = []
		for prime in range(0, max_num):
			if is_prime(prime):
				primes.append(prime)

		total_primes = str(len(primes))
		largest_prime = str(primes[-1])
		smallest_prime = str(primes[0])
		print('\n[+] total bilangan prima 1 s/d %s : %s' % (max_num, total_primes))
		print('[+] bilangan prima terbesar : %s' % (largest_prime))
		print('[+] bilangan prima terkecil : %s\n' % (smallest_prime))

		x = 0
		while x < len(primes):
			for value in primes:
				x = x + 1
				print(str(x)+' Yaitu : '+str(value))

	if __name__ == '__main__':
		print("")
		max = int(raw_input('[*] masukan nilai max : '))
		find_primes(max)

def pegawai():
	stop = False
	pegawai = [ ]
	def tambah():

		stop = False
		i = 0

	#Mengisi Array
		while(not stop):
			pegawai_baru = raw_input("Inputkan nama pegawai yang ke-{}: ".format(i+1))
			pegawai.append(pegawai_baru)
		# methode append menambahkan list/item dari belakang 
		# Increment 1
			i += 1

			tanya = raw_input("Mau isi lagi ? (y/t): ")
			if(tanya == "t"):
				kembali()
	def lihat():
	# Cetak Semua Pegawai
		print "\n"
		print "=" * 100
		print "Kamu memiliki {} pegawai" .format(len(pegawai))
		for hb in pegawai:
			print "- {}" .format(hb)
		print "\n"
		pilih = raw_input("mau kembali ke menu ? (y/t): ")
		if(pilih == "y"):
			kembali()
		else:
			lihat()
	#fungsi len digunakan untuk mengambil panjang list

	def kembali():
		print "*" * 100
		print "1. Tambah Data Pegawai \n"
		print "2. Lihat Data Pegawai \n"
		print "3. Hapus Data Pegawai \n"
		print "4. Exit \n"

		pilih = input("Masukkan Pilihan (1/2/3/4)  = ")
		if(pilih == 1):
			tambah()
		elif(pilih == 2) :
			lihat()
		elif(pilih == 3):
			hapus()
		elif(pilih == 4):
			stop = True
		else:
			stop = True
	def hapus():
		a = 0
		print "Kamu memiliki {} pegawai" .format(len(pegawai))
		for hb in pegawai:
			print "- {}" .format(hb)
		print "\n"
		a = input("hapus data pegawai yang ke - ")
		del pegawai[a-1]
		print "Data Pegawai telah dihapus "
		kembali()

	kembali()
	
def kuis_sosmed():
	from random import randint

	count = 0
 

	Soal = ["Social Media buatan Mark zuck...? ",
     			"Social Media yang eksis dengan awake sleep? ",
     			"Microblogging yang gambar burung apa hayo? ",
     			"Social Media yang populer dengan photo?",
     			"Social Media yang logonya hampir sama dengan Path  ",
     			"Social Media buat pekerja itu namanya: ",
     			"Planet Python di Indonesia itu hanya: "]
	Jawab = ["facebook",
    	 			"path",
     				"twitter",
     				"instagram",
     				"pinterest",
     				"linkedin",
     				"planpin"]
     
	link = ["http://www.facebook.com",
            	"http://Path.com",
            	"http://twitter.com",
            	"http://Instagram.com",
            	"http://Pinterest.com",
           	 "http://linkedin.com",
            	"http://planet.python.or.id/"]

	i = randint(0, 7)
	answer = raw_input("Pertanyaan 1 : " + Soal[i])
	if answer.lower() == Jawab[i]: 
    		print "Yeee Benar"
    		count = count + 1
	else: 
    		print "Yaah Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]


	i = randint(0, 7) 
	answer = raw_input("\nPertanyaan 2 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yaah Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

	i = randint(0, 7)
	answer = raw_input("\nPertanyaan 3 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yahh Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

	i = randint(0, 7) 
	answer = raw_input("\nPertanyaan 4 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yahh Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

	i = randint(0, 7)
	answer = raw_input("\nPertanyaan 5 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yahh Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

	i = randint(0, 7) 
	answer = raw_input("\nPertanyaan 6 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yahh Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

	i = randint(0, 7)
	answer = raw_input("\nPertanyaan 7 : " + Soal[i])
	if answer.lower() == Jawab[i]:
    		print "Yee Benar"
    		count = count + 1
	else:
    		print "Yahh Salah \nJawaban Benar : " + Jawab[i]
    		print "Pengen Coba? Kunjungi : " + link[i]

		print "\n %d jawaban benar" % (count)
		print "\nNilai : %d persen\n" % (count / float(7) * 100)

def tes():
	print("TUNGGU UPDATE-AN SELANJUTNYA YA GAN\n"*3000)

def keluar():
	print "\033[93mTERIMA KASIH TELAH MENGGUNAKAN TOOLS KAMI:)"
	print
	sys.exit()

#Program Utama
print
time.sleep(0.5)
print "\033[92mSELAMAT DATANG DI PROGRAM SEDERHANA KAMI"
print "------------------------------------------"
pilihan = 'y'
while (pilihan != 't'):
	menu()
	pilih = input("Masukkan pilihan : ")

	if pilih == 1:
       		        biodata()
	elif pilih == 2:
	       	        tahunkabisat()
	elif pilih == 3:
			nembakcewek()
	elif pilih == 4:
			lele()
	elif pilih == 5:
			saldo()
	elif pilih == 6:
			cuaca()
	elif pilih == 7:
			prima()
	elif pilih == 8:
			pegawai()
	elif pilih == 9:
			kuis_sosmed()
	elif pilih == 10:
			tes()
	elif pilih == 0:
			keluar()
	else :
        	        print ("MASUKAN PILIHAN YG BENER -_-")
			print
	pilihan = raw_input("Kembali Ke Menu Pilihan? (y/t) ")
	continue
