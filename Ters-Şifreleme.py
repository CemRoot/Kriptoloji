# Kullanıcadan veri alınıp değişkenine aktarılıyor.
veri = input("Lütfen bir mesaj giriniz: ") # Kullanıcadan veri alınıyor.
sifreli_veri = "" # Sifreli veri değişkeni oluşturuluyor.

# Girilen verinin uzunluğu alınır.
veri_uzunluğu = len(veri) - 1 # Uzunluk değişkeni oluşturuluyor.

# girilen metnin tamamı parçalanarak ters çevrilir.
while veri_uzunluğu >= 0:
    sifreli_veri = sifreli_veri + veri[veri_uzunluğu] # Sifreli veri değişkenine parçalama yapılır.
    veri_uzunluğu = veri_uzunluğu - 1 # Uzunluk değişkeni azaltılır.
# Şifreli veri ekrana yazdırılır.
print("Şifreli veri: ", sifreli_veri) # Şifreli veri ekrana yazdırılır.

