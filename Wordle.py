import random
from termcolor import colored

rakamlar1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dogru = []
rastgele_kelime = ["BADEM", "SELAM", "NABER", "ARABA", "KARAR", "LAMBA", "SEHPA"]
oyun = ["*", "*", "*", "*", "*"]
kontrol = ["*", "*", "*", "*", "*"]

bir = ""
iki = ""
uc = ""
dort = ""
bes = ""


def ekran():
    print(oyun)


while True:
    while True:
        kelime = input("5 harfli kelime girin veya rastgele kelime için 'r' yazın: ")
        hak = int(input("Kaç deneme  hakkı olsun?"))
        if(hak < 1):
            print("Lütfen geçerli bir sayı giriniz.")
            continue
        elif(hak not in rakamlar1):
            print("Lütfen geçerli bir sayı giriniz.")
            continue
        if (kelime == "r" or kelime == "R"):
            dogru.extend(random.choice(rastgele_kelime))
            break
        elif (len(kelime) == 5):
            dogru.extend(kelime)
            break

        if (kontrol in rakamlar1):
            print("Lütfen kelime girin")
            continue
        if (len(kelime) != 5):
            print("Lütfen geçerli bir kelime girin.")
            continue

    while True:
        print("Kalan deneme hakkınız: ",hak)
        if(hak == 0):
            print("Deneme hakkınız kalmadı. Doğru kelime: ",dogru)
            break
        ekran()
        deneme = input("Tahmin: ")
        if(deneme != ""):
            hak -= 1
        if (deneme in rakamlar1):
            print("Lütfen kelime girin")
            continue
        if (len(deneme) != 5):
            print("Lütfen geçerli bir kelime girin.")
            continue
        if (len(deneme) == 5):
            for i in range(0, 5):
                kontrol[i] = deneme[i]
            if (kontrol == dogru):
                print("Tebrikler doğru yanıtı buldunuz!")
                print(dogru)
                break
            for i in range(0,5):
                oyun[i] = kontrol[i]
            bir = kontrol[0]
            iki = kontrol[1]
            uc = kontrol[2]
            dort = kontrol[3]
            bes = kontrol[4]
            """ 1 """
            if (bir == dogru[0]):
                print(colored(bir,"green"),end="")
            elif (bir in dogru):
                print(colored(bir,"yellow"),end="")
            elif (bir not in dogru):
                print(colored(bir,"red"),end="")

            """ 2 """
            if (iki == dogru[1]):
                print(colored(iki,"green"),end="")
            elif (iki in dogru):
                print(colored(iki,"yellow"),end="")
            elif (iki not in dogru):
                print(colored(iki,"red"),end="")

            """ 3 """
            if (uc == dogru[2]):
                print(colored(uc, "green"), end="")
            elif (uc in dogru):
                print(colored(uc, "yellow"), end="")
            elif (uc not in dogru):
                print(colored(uc, "red"), end="")

            """ 4 """
            if (dort == dogru[3]):
                print(colored(dort, "green"), end="")
            elif (dort in dogru):
                print(colored(dort, "yellow"), end="")
            elif (dort not in dogru):
                print(colored(dort, "red"), end="")

            """ 5 """
            if (bes == dogru[4]):
                print(colored(bes, "green"), end="")
            elif (bes in dogru):
                print(colored(bes, "yellow"), end="")
            elif (bes not in dogru):
                print(colored(bes, "red"), end="")
            print("\n")

    a = input("Tekrar oynamak için 'enter' a bas")
    oyun = ["*", "*", "*", "*", "*"]
    kontrol = ["*", "*", "*", "*", "*"]
    dogru = []
    bir = ""
    iki = ""
    uc = ""
    dort = ""
    bes = ""
    if(a != ""):
        break