def menuutama():
    print("")
    n = raw_input('masukkan nama Konsumen: ')
    print 'Nama Konsumen :',n
    print """Masukkan Pilihan
           1. Bayar
           2. Keluar"""
    print("")


def menuutama1():
    print """Masukkan Pilihan
           1. Bayar
           2. Keluar"""
    print("")
    
            


class makanan():
    def bakso (self,x):
        jmlhpsn = x * 7000
        pajak = jmlhpsn * 0.1
        total = jmlhpsn + pajak
        print 'Harga Bakso = Rp 7000'
        print ''
        print 'Total Makanan = Rp ',jmlhpsn
        print 'Pajak = Rp ',pajak
        print'___________________________________+'
        print 'Total Seluruhnya = Rp ', total
        return jmlhpsn
    def mieayam (self,x):
        jmlhpsn = x * 6000
        pajak = jmlhpsn * 0.1
        total = jmlhpsn + pajak
        print 'Harga Mie Ayam = Rp 6000'
        print ''
        print 'Total Makanan = Rp ',jmlhpsn
        print 'Pajak = Rp ',pajak
        print'___________________________________+'
        print 'Total Seluruhnya = Rp ', total
        return jmlhpsn
    def sotoayam (self,x):
        jmlhpsn = x * 7500
        pajak = jmlhpsn * 0.1
        total = jmlhpsn + pajak
        print 'Harga Soto Ayam = Rp 7500'
        print ''
        print 'Total Makanan = Rp ',jmlhpsn
        print 'Pajak = Rp ',pajak
        print'___________________________________+'
        print 'Total Seluruhnya = Rp ', total
        return jmlhpsn
    def sotomie (self,x):
        jmlhpsn = x * 8000
        pajak = jmlhpsn * 0.1
        total = jmlhpsn + pajak
        print 'Harga Soto Mie = Rp 8000'
        print ''
        print 'Total Makanan = Rp ',jmlhpsn
        print 'Pajak = Rp ',pajak
        print'___________________________________+'
        print 'Total Seluruhnya = Rp ', total
        return jmlhpsn
    def gadogado (self,x):
        jmlhpsn = x * 5000
        pajak = jmlhpsn * 0.1
        total = jmlhpsn + pajak
        print 'Harga Gado-gado = Rp 5000'
        print ''
        print 'Total Makanan = Rp ',jmlhpsn
        print 'Pajak = Rp ',pajak
        print'___________________________________+'
        print 'Total Seluruhnya = Rp ', total
        return jmlhpsn
    
class minuman():
    def airmineral (self,z):
        jmlhpsn1 = z * 3000
        pajak = jmlhpsn1 * 0.1
        total = jmlhpsn1 + pajak
        print 'Harga Air Mineral = Rp 3000'
        print ''
        print 'Total Minuman = Rp ',jmlhpsn1
        print 'Pajak = Rp ',pajak
        print '__________________________________+'
        print 'Total Seluruhnya = Rp ',total
        return jmlhpsn1
    def estehmanis (self,z):
        jmlhpsn1 = z * 2000
        pajak = jmlhpsn1 * 0.1
        total = jmlhpsn1 + pajak
        print 'Harga Es Teh Manis = Rp 2000'
        print ''
        print 'Total Minuman = Rp ',jmlhpsn1
        print 'Pajak = Rp ',pajak
        print '__________________________________+'
        print 'Total Seluruhnya = Rp ',total
        return jmlhpsn1
    def esjeruk (self,z):
        jmlhpsn1 = z * 3500
        pajak = jmlhpsn1 * 0.1
        total = jmlhpsn1 + pajak
        print 'Harga Es Jeruk = Rp 3500'
        print ''
        print 'Total Minuman = Rp ',jmlhpsn1
        print 'Pajak = Rp ',pajak
        print '__________________________________+'
        print 'Total Seluruhnya = Rp ',total
        return jmlhpsn1
    def jusalpukat (self,z):
        jmlhpsn1 = z * 5000
        pajak = jmlhpsn1 * 0.1
        total = jmlhpsn1 + pajak
        print 'Harga Jus Alpukat = Rp 5000'
        print ''
        print 'Total Minuman = Rp ',jmlhpsn1
        print 'Pajak = Rp ',pajak
        print '__________________________________+'
        print 'Total Seluruhnya = Rp ',total
        return jmlhpsn1
    def jusmelon (self,z):
        jmlhpsn1 = z * 4000
        pajak = jmlhpsn1 * 0.1
        total = jmlhpsn1 + pajak
        print 'Harga Jus Melon = Rp 4000'
        print ''
        print 'Total Minuman = Rp ',jmlhpsn1
        print 'Pajak = Rp ',pajak
        print '__________________________________+'
        print 'Total Seluruhnya = Rp ',total
        return jmlhpsn1


def back_menu():
    print ('Apakah anda ingin memesan lagi? [Y/N] :')
    back = raw_input().upper()
    if back == "Y":
        menuutama1()
        pilihan()
        print("")
    else:
        print 'Terima Kasih !'
        exit


def pilihan():
    
    x = input ("Masukan Pilihan : ")
    if x == 1:
          mk = makanan()
    pil=1
    while pil !=6:
        print """Pilih Makanan
                       1. BAKSO
                       2. MIE AYAM
                       3. SOTO AYAM
                       4. SOTO MIE
                       5. GADO - GADO
                       6. Minuman"""
        pil = int (input('Masukkan pilihan anda : '))
        print
        if pil == 1:
            print ("")
            x = input ('Jumlah porsi : ')
            mk.bakso(x)
            pil=6
            
        if pil == 2:
            print ("")
            x = input ('Jumlah porsi : ')
            mk.mieayam(x)
            pil=6
            
        if pil == 3:
            print ("")
            x = input ('Jumlah porsi : ')
            mk.sotoayam(x)
            pil=6
            
        if pil == 4:
            print ("")
            x = input ('Jumlah porsi : ')
            mk.sotomie(x)
            pil=6
            
        if pil == 5:
            print ("")
            x = input ('Jumlah porsi : ')
            mk.gadogado(x)
            print
            pil=6
            
                                    


    pil = 0
    mn = minuman()
    while pil !=6:
        print """Pilih Minuman
                        1. Air mineral
                        2. Es teh manis
                        3. Es Jeruk
                        4. Jus Alpukat
                        5. Jus Melon"""
        pil = int (input('Masukkan pilihan anda : '))
        print
        if pil == 1:
            print ("")
            z = input ('Jumlah gelas : ')
            mn.airmineral(z)
            pil=6
            back_menu()
        if pil == 2:
            print ("")
            z = input ('Jumlah gelas : ')
            mn.estehmanis(z)
            pil=6
            back_menu()
        if pil == 3:
            print ("")
            z = input ('Jumlah gelas : ')
            mn.esjeruk(z)
            pil=6
            back_menu()
        if pil == 4:
            print ("")
            z = input ('Jumlah gelas : ')
            mn.jusalpukat(z)
            pil=6
            back_menu()
        if pil == 5:
            print ("")
            z = input ('Jumlah gelas : ')
            mn.jusmelon(z)
            pil=6
            back_menu()
        else:
          exit
menuutama()
pilihan()