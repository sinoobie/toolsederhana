import random

print("Permainan Batu Gunting Kertas")
print("Pilihan :")
print("1. Batu")
print("2. Gunting")
print("3. Kertas")

def permainan():
    kamu = int(input("Masukan pilihanmu: "))
    kom = random.choice(["Batu", "Gunting", "Kertas"])
    if kamu == 1:
        print("Kamu     : Batu")
        print("Komputer :", kom)
        if kom == "Batu":
            print("\tDraw")
        if kom == "Gunting":
            print("\tLu menang")
        if kom == "Kertas":
            print("\tLu kalah")
    if kamu == 2:
        print("Kamu     : Gunting")
        print("Komputer :", kom)
        if kom == "Batu":
            print("\tKamu kalah")
        if kom == "Gunting":
            print("\tDraw")
        if kom == "Kertas":
            print("\tLu Menang")
    if kamu == 3:
        print("Kamu     : Kertas")
        print("Komputer :", kom)
        if kom == "Batu":
            print("\tLu menang")
        if kom == "Gunting":
            print("\tLu kalah")
        if kom == "Kertas":
            print("\tDraw")
    if kamu >= 4:
        print("Pilihanmu salah!!!")
permainan()
