# kalıcı hafıza - disk (hdd,ssd)

# csv, excel, pdf

# Dosya -> Yavaş işlem, karmaşık.
# Veritabanı -> .mdf .db 

#with -> performans yönetimi için
with open("dosya.txt", "r", encoding="utf-8") as file:
    print(f"Kalıcı hafızadan okunan veri: {file.read()}")

value = input("Dosyaya yazmak istediğiniz değeri belirtiniz:")

with open("dosya.txt", "a", encoding="utf-8") as file:
  file.write(value)

# .csv -> Veri seti dosyalarıyla

#f = open("dosya.txt", "r", encoding="utf-8")
#content = f.read()
#print(content)
#f.close()

#f2 = open("dosya.txt", "a", encoding="utf-8")
#f2.write("Yeni içerik")
#f2.close()