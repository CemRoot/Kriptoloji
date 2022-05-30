# Şifreleme yapılacak fonksiyon
def sifre(mesaj, adim):
    sonuc = ""

    # Karater parçalama
    for i in range(len(mesaj)):
        char = mesaj[i]

        # şifrelenmesi büyük  karakterler
        if char.isupper(): # Karakter büyükse
            # Karakterin ASCII kodunu alır. Karakterin ASCII kodunu adım değeri ile toplar.
            # Karakterin ASCII kodunu yeni ASCII kodu ile değiştirir.
            # Karakterin yeni ASCII koduna göre yeni karakter oluşturulur.
            sonuc += chr((ord(char) + adim - 65) % 26 + 65)

        # şifrelenmesi küçük karakterler
        else:# Karakter küçükse
            sonuc += chr((ord(char) + adim - 97) % 26 + 97)
            #ord() fonksiyonu içerisine gönderilen unicode, karakterin ASCII tablosundaki karşılığını vermektedir.
            #((ord(char) + adim - 97) buradaki komut ile gönderdiğimiz harfin ASCII tab. konumu bulunuyor
            # ASCII tablosunda küçük harfler 97'den başlar. Büyük harfler ise 65'den başlayıp 90'da bitmektedir.
            # Büyük harflerin sayısı ise 26'dır bu nedenle gönderilen harfin konumu tespit edilir ve sayıya çevrilir.
            # Karakterin konumu tespit edilir ve adım değeri ile toplanır.

    return sonuc


mesaj = "PYTHON"
adim = 5
print("Mesaj:" + mesaj)
print("Adım sayısı:" + str(adim))
print("Şifrelenmiş mesaj:" + sifre(mesaj, adim))
