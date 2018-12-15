print ("")
print ("------ PROGRAM PYTHON UNTUK MENGHITUNG SALDO ------")
print ("")
print ("by : KANG NEWBIE")
print ("")

tabungan = int(input("Masukkan jumlah tabungan :"))
lama = int(input("Masukkan jumlah lama menabung (bulan) :"))
 
if tabungan < 1000000 :
 sukuBunga = 0.03
 saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
 print("")
 print("Karena tabungan anda dibawah 1.000.000,\nbunga yg anda dapatkan 3%")
 print("Saldo anda selama " + str (lama) + " bulan, adalah " +str (saldoAkhir))
 print("")

elif tabungan > 1000000 :
 sukuBunga = 0.04
 saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
 print("")
 print("Karena tabungan anda diatas 1.000.000,\nbunga yang anda dapatkan 4%")
 print("Saldo anda selama " + str (lama) + " bulan, adalah " +str (saldoAkhir))
 print("")
