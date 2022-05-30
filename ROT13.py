import codecs  # for codecs.encode()

msg = input("Enter a message: ") # Kullanıcadan veri alınıyor.
password = codecs.encode(msg, 'rot_13') # Kullanıcadan girilen veri rot_13 ile şifreleniyor.

print("Message:", msg) # Kullanıcadan girilen veri ekrana yazdırılıyor.
print("Encoded message:", password)# Kullanıcadan girilen veri rot_13 ile şifrelenmiş halini ekrana yazdırılıyor.

undecoded = codecs.decode(password, 'rot_13') # Şifreli veri rot_13 ile şifresi çözülüyor.
print("Encrypted message: ", undecoded) # Şifreli veri ekrana yazdırılıyor.
