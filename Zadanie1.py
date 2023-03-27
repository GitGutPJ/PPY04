import math


def fun(dlugoscPodlogi, szerokoscPodlogi, dlugoscPanel, szerokoscPanel, pakietPaneli):
    wielkoscPodlogi = (dlugoscPodlogi*szerokoscPodlogi)
    wielkoscPodlogi += wielkoscPodlogi*0.1
    wielkoscPanelu = (dlugoscPanel*szerokoscPanel)
    iloscPaneli = wielkoscPodlogi/wielkoscPanelu
    iloscPaneli=math.ceil(iloscPaneli)
    iloscPaneli/=pakietPaneli
    iloscPaneli = math.ceil(iloscPaneli)
    return iloscPaneli


dlPodlogi = input("Podaj dlugosc podlogi")
dlPodlogi = int(dlPodlogi)
szPodlogi = input("Podaj szerokosc podlogi")
szPodlogi = int(szPodlogi)
dlPaneli = input("Podaj dlugosc paneli")
dlPaneli = int(dlPaneli)
szPaneli = input("Podaj szerokosc paneli")
szPaneli = int(szPaneli)
iloscPakietow = input("Ilosc pakietow")
iloscPakietow = int(iloscPakietow)

print("Ilosc paneli w: ", fun(dlPodlogi, szPodlogi, dlPaneli, szPaneli,iloscPakietow))
