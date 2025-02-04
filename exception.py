# Hata Yönetimi

print("Hata Yönetimi Başladı")

# Kullanıcıdan 2 sayı al, bunların bölümünü print et.
# try-catch-finally blokları -> try-except-finally-else

try:
    sayi1 = input("Lütfen ilk sayıyı giriniz: ") # casting "1", "abc","12345", "True", 1->"1"
    sayi1 = int(sayi1)

    sayi2 = input("Lütfen ikinci sayıyı giriniz: ") # casting "1", "abc","12345", "True", 1->"1"
    sayi2 = int(sayi2)

    print(f"Sonuç: {sayi1/sayi2}")

    print("Hata Yönetimi Bitti.")
    #...
except ZeroDivisionError:
    print("İkinci sayı olarak 0 girilemez..")
except:
    print("Hata fırladı..")
else: # hiç bir hata fırlamazsa kullanılacak.
    print("Hata yok")
finally:
    print("En son çalışacak kod.")
#
