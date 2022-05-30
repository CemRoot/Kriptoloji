def rot13(msg):  # rot13 fonksiyonu tanımlandı.
    root13 = ''  # rot13 fonksiyonunun çıktısının tutulacağı değişken tanımlandı.
    alfabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'  # alfabet tanımlandı.

    for i in msg:  # msg değişkenindeki karakterleri alır.
        if i in alfabet:  # alfabet değişkenindeki karakterler için kontrol yapılır.
            root13 = root13 + alfabet[(alfabet.find(i) + 13) % len(
                alfabet)]  # alfabet değişkenindeki karakterlerin 13 adet önceki karakterleri alır.
        else:  # alfabet değişkeninde bulunmayan karakterler için kontrol yapılır.
            root13 = root13 + i  # alfabet değişkeninde bulunmayan karakterler için karakterlerin kendileri kullanılır.
    return root13  # rot13 fonksiyonunun çıktısının döndürülmesi.


msg = input("Enter a message: ")  # Kullanıcadan veri alınıyor.
print("Message:", msg)  # Kullanıcadan girilen veri ekrana yazdırılıyor.
print("Encoded message:", rot13(msg))  # Kullanıcadan girilen veri rot13 ile şifrelenmiş halini ekrana yazdırılıyor.
print("Encrypted message: ",
      rot13(rot13(msg)))  # Kullanıcadan girilen veri rot13 ile şifrelenmiş halini rot13 ile şifresi çözülüyor.
