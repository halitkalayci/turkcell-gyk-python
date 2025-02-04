#Modüller
#import edilebilen modüller -> built-in (pythonda kurulu), kendi modüllerim (projedeki diğer .py dosyaları), 3. taraf kütüphaneler
#

#built-in -> math
# import math # dışardan built-in modül import etmek -> 2 farklı yöntem
# import math -> tüm matematik kütüphanesini import eder.
from math import sqrt as karekok, factorial as faktoriyel # math kütüphanesinden yalnızca sqrt,factorial import eder.
#ctrl+space -> intellisense
sayi1 = int(input())

sonuc = karekok(sayi1)
print(sonuc)

sonuc2 = faktoriyel(sayi1)
print(sonuc2)

