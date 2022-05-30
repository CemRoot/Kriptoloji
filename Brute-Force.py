"""Sezar şifrelemesinin kırılması da Brute Force tekniği kullanılarak yapılır.
    Bu tekniğe göre her bir olasılık denenerek bulunur."""

sifre = (input("Lütfen bir şifre giriniz: "))
dize = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(dize)):
    donusum = ''
    for karakter in sifre:
        if karakter in dize:
            num = dize.find(karakter)
            num = num - i
            if num < 0:
                num = num + len(dize)
            donusum = donusum + dize[num]
        else:
            donusum = donusum + dize[num]
    print('Çözülme aşaması #%s: %s' % (i, donusum))
