"""pip install pyDES"""  # first install pyDES
import pyDes

data = "Python ile kriptoloji uygulamalari"
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
# Burada kriptolojik verilerin şifrelenmesi için kullanılacak kriptolojik algoritmayı tanımladık.
# Şifreleme için kullanılacak veriyi ve şifreleme için kullanılacak kriptolojik algoritmayı tanımladık.
d = k.encrypt(data)  # Şifrelenmiş veriyi d değişkenine atadık.
print("Şifrelenmiş veri: %r" % d)  # Şifrelenmiş veriyi ekrana yazdırdık.
print("Şifresi çözülmüş veri: %r" % k.decrypt(d))  # Şifresi çözülmüş veriyi ekrana yazdırdık.
"""
>>>Şifrelenmiş veri: b'\x1e\xf1\xf60\xba\xaaAN\xb1\xe6\x97\xde\xac\x1c$\xd8\xff\xe9G1K\x1c=\x8b\x80\xa3\xadg\xea \xc3\tq\x96m\xdd\xecH\x10\xcc'
Şifresi çözülmüş veri: b'Python ile kriptoloji uygulamalari'
"""
#DES şifreleme metni bloklar halinde şifrelemektedir.
