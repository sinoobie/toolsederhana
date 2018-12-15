
gaji=0
pengeluaran=[]
nominalPengeluaran=[]


def menu():
    print("=================================")
    print("=========== Menu Utama ==========")
    print("=================================")
    print("1. Hitung pengeluaran")
    print("2. Report Pengeluaran")
    print("0. Keluar")
    print("---------------------------------")
    try :
        pilih=int(input("Masukan pilihan > "))
    except ValueError:
        print("format tipe data input salah")
        menu()
    else :
        if pilih == 1:
            hitungGaji()
        elif pilih == 2:
            report()
        elif pilih == 0:
            exit()
        else :
            print("Maaf pilihan tidak ada !!!!")
            menu()



def hitungGaji():
    global gaji
    print("---------- Menu Input Gaji ----------")
    print("1. Lanjut")
    print("2. Kembali")
    print("0. Keluar")
    print("--------------------------------------")
    try :
        pilih = int(input("Masukan Pilihan > "))
    except ValueError:
        print("format tipe data input salah")
        hitungGaji()
    else :
        if pilih ==1:
            try :
                inputGaji = int(input("Masukan nominal Gaji Rp. > "))
            except ValueError:
                print("format tipe data input salah")
                hitungGaji()
            else :
                gaji = gaji + inputGaji
                hitungPengeluaran()
        elif pilih == 2:
            menu()
        elif pilih == 0:
            exit()

def hitungPengeluaran():
    global pengeluaran,nominalPengeluaran
    print("---------- Menu Pengeluaran ----------")
    status=True
    while(status):
        try :
            inputPengeluaran = input("Masukan untuk apa pengeluaran > ")
            inputNominalPengeluaran = int(input("Masukan Nominal Pengeluaran Rp. > "))
        except ValueError:
            print("format tipe data input salah")
            hitungPengeluaran()
        else :
            pengeluaran.append(inputPengeluaran)
            nominalPengeluaran.append(inputNominalPengeluaran)
            print("1. Lanjut")
            print("2. Tidak")
            print("------------------------------------")
            try :
                pilih = int(input("Masukan Pilihan > "))
            except ValueError:
                print("format tipe data input salah")
                hitungPengeluaran()
            else :
                if pilih == 1:
                    status=True
                elif pilih == 2:
                    status == False
                    menu()
                else :
                    print("Maaf pilihan tidak ada, harap periksa kembali")
                    clean()
                    hitungPengeluaran()

def report():
    global gaji,nominalPengeluaran,pengeluaran
    print("============= Report Pengeluaran ===========")
    print("Gaji Anda Rp.",gaji)
    jumlahPengeluaran=0

    for i,x in enumerate(pengeluaran):
        jumlahPengeluaran = jumlahPengeluaran + nominalPengeluaran[i]
        print(i+1,x,"\t", nominalPengeluaran[i])

    gaji = gaji - jumlahPengeluaran
    print("sisa duit anda Rp.",gaji)
    print("--------------------------------------------")
    print("1. Reset Program")
    print("2. Ke Menu Utama")
    print("0. Keluar")
    try :
        pilih = int(input("Masukan pilihan > "))
    except ValueError:
        print("format tipe data input salah")
        exit()
    else :
        if pilih == 1:
            gaji=0
            pengeluaran=[]
            nominalPengeluaran=[]
            print("Reset Berhasil !!!!!")
            report()
        elif pilih == 2:
            menu()
        elif pilih == 0:
            exit()
        else :
            print("Maaf Pilihan tidak ada !!!!")
            report()




if __name__ == "__main__":
    menu()