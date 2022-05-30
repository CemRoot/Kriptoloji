import base64

# base64.b64encode("Python ile kriptoloji") şeklinde kullanım hata verecektir.
sifreli_veri = base64.b64encode(b"Python ile kriptoloji")  # doğru kullanım
sifre_coz = base64.b64decode(sifreli_veri)
print("Sifreli Veri:", sifreli_veri)
print("Çözülmüş Veri:", sifre_coz)
