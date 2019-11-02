while 1:
    def islemler(islem):
        if islem == 1:
            isim = str(input("İsim: "))
            birim = str(input("Birim fiyat: "))
            adet = str(input("Alınan adet: "))
            ucret = str(input("Ödenen ücret: "))
            musteri_ekle(isim, birim, adet, ucret)
        elif islem == 2:
            musteri_duzenle()
        elif islem == 3:
            musteri_ara()
        elif islem == 4:
            musteri_sil()
        else:
            exit()


    def musteri_ekle(isim, birim, adet, ucret):
        with open("musteriler.txt", "a", encoding="utf-8") as file:
            file.write(isim + ":" + birim + ":" + adet + ":" + ucret + "\n")


    def musteri_duzenle():
        deger = input("Düzenlemek istediğiniz değer: ")
        degisecek = input("Yeni değeri girin: ")

        yazdirilacak = []

        with open("musteriler.txt", "r", encoding="utf-8") as file:
            dizi = file.readlines()

            for i in dizi:
                yenideger = i.split(":")
                if yenideger[0] == deger:
                    yenideger[0] = degisecek
                yazdirilacak.append(yenideger[0] + ":" + yenideger[1] + ":" + yenideger[2] + ":" + yenideger[3])

        with open("musteriler.txt", "w", encoding="utf-8") as file:
            for i in yazdirilacak:
                file.write(i)


    def musteri_ara():
        with open("musteriler.txt", "r", encoding="utf-8") as file:
            isim = input("Müşteri adı girin: ")
            for i in file.readlines():
                if isim in i:
                    i = i[:-1]
                    print(i)


    def musteri_sil():
        silinecek = input("Silmek istediğiniz müşteri: ")
        yazdırılacak = []

        with open("musteriler.txt", "r", encoding="utf-8") as file:
            dizi = file.readlines()

            for i in dizi:
                if i.split(":")[0] == silinecek:
                    pass
                else:
                    yazdırılacak.append(i)

        with open("musteriler.txt", "w", encoding="utf-8") as file:
            for i in yazdırılacak:
                file.write(i)


    print("""Müşteri Uygulamasına Hoşgeldiniz...
    Yapılabilecek işlemler:
    1.Müşteri Ekle
    2.Müşteri Düzenle
    3.Müşteri Ara
    4.Müşteri Sil
    5.Çıkış""")
    islem = int(input("Lütfen yapmak istediğiniz işlemi seçin: "))
    islemler(islem)
