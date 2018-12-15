print(' ')
print(' Created By :')
print(' KANG NEWBIE')
print(' ')

def memilih():
    a = input('Pilihan (Masukkan angka) \n1-Konversi Suhu \n2-Menghitung Jarak'
              '\n3-Menghitung Energi \n4-Menghitung Gaya Coulomb \n5-Keluar'
              '\n Pilihan : ')
    return a
pilihan = 1
while pilihan <= 5 :
    pilihan = int(memilih())
    if pilihan == 1:
        print('Konversi suhu dari celcius ke fahrenheit, reamur, dan kelvin')
        clc = float(input('Masukkan suhu celcius : '))
        print('')
        fhr = (9./5)*clc+32
        rmu = (4./5)*clc
        klv = clc+273
        print('Hasil Perhitungan Konversi Suhu')
        print('Suhu celcius : %g' %(clc))
        print('Suhu fahrenheit : %g' %(fhr))
        print('Suhu reamur : %g' %(rmu))
        print('Suhu kelvin : %g' %(klv))
        continue
    elif pilihan == 2:
        print('Menghitung jarak sebuah kendaraan yang bergerak')
        v0 = float(input('Berapa kecepatan awal kendaraan? (m/s) : '))
        a = float(input('Berapa percepatan kendaraan? (m/s2) : '))
        t = float(input('Berapa lama waktu bergerak? (s) : '))
        jarak = (v0*t)+(0.5*a)*t*t
        print('')
        print('Jarak tempuh : %g meter'%(jarak))
        print('\n')
        continue
    elif pilihan == 3:
        print('Menghitung energi kinetik, energi potensial dan energi mekanik')
        g = 9.8 #(m/s2)
        m = float(input('Masukkan massa benda (kg) : '))
        v = float(input('Masukkan kecepatan benda(m/s) (untuk energi kinetik) : '))
        h = float(input('Masukkan ketinggian benda(m) (untuk energi potensial) : '))
        ek = 0.5*m*(v**2)
        ep = m*g*h
        em = ek+ep
        print('')
        print('Hasil Penghitungan Energi')
        print('Energi kinetik : %g joule'%(ek))
        print('Energi potensial : %g joule' %(ep))
        print('Energi mekanik : %g joule' %(em))
        print('\n')
        continue
    elif pilihan == 4:
        print('Menghitung gaya coulomb')
        k = 9*10**9
        q1 = float(input('Masukkan muatan benda 1 (Q1) (C): '))
        q2 = float(input('Masukkan muatan benda 2 (Q2) (C): '))
        r = float(input('Masukkan jarak antar muatan (m): '))
        coulomb = (k*q1*q2)/r**2
        print('')
        print('Gaya coulomb : %.2f Newton' %(coulomb))
        print('\n')
        continue
    elif pilihan == 5:
        print('       SEKIAN DAN TERIMA KASIH :)')
        print('------------------> <--------------------')
        print('        Wassalamu alaikum Wr. Wb.')
        break
