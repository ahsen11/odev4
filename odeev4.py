# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def kelimeTekrari(kelime, tekrarSayisi):
    for _ in range(tekrarSayisi):
        print(kelime)

kelimeTekrari("yeşil", 2)

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
kenar1=10
kenar2=20
alan=kenar1*kenar2
print("Dikdörtgenin Alanı= ",alan)
çevre=(kenar1+kenar2)*2
print("Dikdörtgenin Çevresi= ",çevre)

# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
import random

def yazi_tura():
    sayi = random.randint(0, 1)
    if sayi == 0:
        return "Yazı"
    else:
        return "Tura"

sonuc = yazi_tura()
print("Sonuç:", sonuc)

# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
def asal_sayilar(sayi1, sayi2):
    asal_sayilar = []
    for sayi in range(sayi1, sayi2 + 1):
        if all(sayi % i != 0 for i in range(2, int(sayi**0.5) + 1)):
            asal_sayilar.append(sayi)
    return asal_sayilar

sayi1 = 17
sayi2 = 24
sonuc = asal_sayilar(sayi1, sayi2)
print(sonuc)

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
def tamBolenler(sayi):
    bolenler = []
    for i in range(1, sayi + 1):
        if sayi % i == 0:
            bolenler.append(i)
    return bolenler

sayi = 27
sonuc = tamBolenler(sayi)
print(sonuc)