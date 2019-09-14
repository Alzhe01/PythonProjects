import random
print("Sayı Tahmin Oyununa Hoşgeldiniz..")
sayi=random.randint(1,101)
while True:
    tahmin=int(input("Tahminin nedir?\n"))
    if tahmin == sayi:
        print("Bravo doğru bildin!\nOYUN BAŞARIYLA TAMAMLANDI...")
        break
    elif tahmin < sayi:
        print("Maalesef tuttuğum sayı daha büyük dostum :(")
    elif tahmin > sayi:
        print("Maalesef tuttuğum sayı daha küçük dostum :(")
