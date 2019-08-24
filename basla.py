while True:
    from time import sleep
    import dosya_olustur
    import random

    class Asal:
        import dosya_olustur
        def AsalmiHesapla(self, asalmi2):
            tutucu = False
            self.asalmi2 = asalmi2
            for i in range(2, self.asalmi2):
                print(i)

                sonuc = self.asalmi2 % i
                if sonuc == 0:
                    tutucu = True

            return tutucu
    print("Hoş GEldiniz..\nLevel: ", dosya_olustur.level)
    giris = input("Devam etmek için 'E'  Çıkmak için 'H' basın: ")
    if giris == 'E' or giris == 'e':
        print("Oyun Başlıyor..\n")
        for i in range(3, 0, -1):
            print(i)
            sleep(1)
    elif giris == 'H' or giris == 'h':
        print("Çıkış yapılıyor")
        for i in range(3, 0, -1):
            print(i)
            sleep(1)
        exit()
    else:
        print("Yanlış Tuşa Bastınız..\nÇıkış yapılıyor..")
        for i in range(3, 0, -1):
            print(i)
            sleep(1)
        exit()
    try:
        f = open("dosya.txt", "r")
        s = f.readlines()
        sabit = False
        for i in s:
            satir = i.split("\n")
            asalmi = satir[0].split(":")[1]
        x=Asal(asalmi)
        sabit=bool(x.AsalmiHesapla())
    except Exception as e:
        print("hata", e.__class__)
    finally:
        f.close()
    cevap = input(asalmi + " sayısı asal mıdır? ('E' veya 'H')\n")
    if cevap == 'E' or cevap == 'e' and sabit == True:
        print("Bravo! Doğru bildin")
        dosya_olustur.level+=1
        tekrar=input("level: "+str(dosya_olustur.level)+"\n Tekrar oynamak ister misin? ('E' veya 'H') : ")
    elif cevap == 'H' or cevap == 'h' and sabit == False:
        print("Bravo! Doğru bildin")
        dosya_olustur.level += 1
        tekrar=input("Devam etmek ister misin? ('E' veya 'H') : ")
    else:
        print("Maalesef, Bilemedin\nLevel seviyesi rastgele düşürülüyor..")
        dosya_olustur.level-=random.randint(1,10)
        tekrar=input("Tekrar oynamak ister misin? ('E' veya 'H') : ")
    if tekrar == 'E' or tekrar == 'e':
        print("Başlıyoruz")
    elif tekrar == 'H' or tekrar == 'h':
        print("Çıkış Yapıldı")
        break
    else:
        print("Yanlış Tuşa Bastınız..\nÇıkış yapılıyor..")
        break