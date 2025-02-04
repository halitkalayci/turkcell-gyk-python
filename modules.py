#Modüller
#import edilebilen modüller -> 
# built-in (pythonda kurulu), 
# kendi modüllerim (projedeki diğer .py dosyaları), 
# 3. taraf kütüphaneler


#built-in -> math
# import math # dışardan built-in modül import etmek -> 2 farklı yöntem
# import math -> tüm matematik kütüphanesini import eder.
from math import sqrt as karekok, factorial as faktoriyel # math kütüphanesinden yalnızca sqrt,factorial import eder.
import account
import requests
#ctrl+space -> intellisense
sayi1 = int(input())

sonuc = karekok(sayi1)
print(sonuc)

sonuc2 = faktoriyel(sayi1)
print(sonuc2)

acc1 = account.Account(500)
acc1.deposit(500)
acc1.withdraw(100)
acc1.print_status()

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    print(response.json())  # JSON yanıtı al
else:
    print("Hata:", response.status_code)