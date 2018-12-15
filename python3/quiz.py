print("sebaiknya anda menggunakan python3 untuk menjalankan program ini")
print()
print("GAME QUIZ ISLAMI\n")

question1 = "SIAPAKAH PENDIRI MASJID AL-AQSHA?"

options1 = "a. Nabi Isa AS\nb. Nabi Nuh AS\nc. Nabi Muhammad SAW\nd. Nabi Ya'kub AS\n"

print(question1)

print(options1)



while True:

    response = input("Silahkan pilih jawaban anda a,b,c atau d\n")

    if response == "d":

        break

    else:
        print("\n\nJAWABAN ANDA KURANG TEPAT, coba lagi !!!")

        while True:
            response = input("Silahkan pilih jawaban anda a,b, atau d\n")
            if response == "d":
                stop = True
                break
            else:
                print("\n\nJAWABAN ANDA KURANG TEPAT, coba lagi !!!")
                stop = True
                break
        if stop:
            break
while True:
    bonus = input("JAWABAN BENAR\nApakah kamu ingin mencoba soal bonus?\nTekan 'y' jika ya dan 'n' jika tidak.\n")

    if bonus == "y":
        print("\n\nSIAPAKAH SAHABAT RASULULLAH SAW YANG MENDAPAT GELAR PEDANG ALLAH TERHUNUS?")
        print("a. Khalid bin Walid\nb. Abdullah bin Umi Maktum\nc. Mushab bin Umeir\nd. Sa'ad bin Abi Waqqas")

        while True:
            response = input("\nSilahkan pilih jawaban anda a,b, atau d\n")

            if response == "a":
                break
            else:
                print("Jawaban anda salah, coba lagi !!!")

            while True:
                response = input("\n\nJAWABAN ANDA KURANG TEPAT, coba lagi !!!")

                if response == "a":
                    stop = True
                    break
                else:
                    print("jawaban anda belum benar !!, anda telah melampaui batas percobaan")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("AFWAN !!, SILAHKAN TEKAN 'y' ATAU 'N' UNTUK JAWABAN ANDA")

question1 = "\nBERAPAKAH JUMLAH TENTARA ISLAM DALAM PERANG UHUD?"
options1 = "a. 300 Orang\nb. 700 Orang\nc. 800 Orang\nd. 900 Orang\n"
print(question1)
print(options1)

while True:
    response = input("Silahkan pilih jawaban anda a,b,c atau d\n")

    if response == "b":
        break
    else:
        print("\n\nJAWABAN ANDA KURANG TEPAT, coba lagi !!!")

        while True:
            response = input("Silahkan pilih jawaban anda a,b, atau d\n")

            if response == "b":
                stop = True
                break
            else:
                print("\n\nJAWABAN ANDA KURANG TEPAT, coba lagi !!!")
                stop = True
                break
        if stop:
            break
            break
while True:
    bonus = input("JAWABAN BENAR\nApakah kamu ingin mencoba soal bonus?\nTekan 'y' jika ya dan 'n' jika tidak.\n")

    if bonus == "y":
        print("\nBERAPA LAMA MASA UTSMAN BIN AFFAN MENJABAT SEBAGAI KHALIFAH?")
        print("a. 12 TH\nb. 13 TH\nc. 14 TH\nd. 15 TH")

        while True:
            response = input("\nSilahkan pilih jawaban anda a,b, atau d\n")

            if response == "a":
                break
            else:
                print("Jawaban anda salah, coba lagi !!!")

            while True:
                response = input("\n\nJAWABAN ANDA KURANG TEPAT, coba lagi !!!")


                if response == "a":
                    stop = True
                    break
                else:
                    print("jawaban anda belum benar !!, anda telah melampaui batas percobaan")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("AFWAN !!, SILAHKAN TEKAN 'y' ATAU 'N' UNTUK JAWABAN ANDA")
