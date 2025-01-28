print("Hello World")

# değişkenler
x = 5 # değişken türü
print(x)
print(type(x)) # integer => tam sayı
#
text = "Turkcell" # string
print(text)

text = "Kodlamaio"
print(text)

# immutable (value) (değer tip)
a = 5
b = a
b = 3
print(b)
print(a)

# mutable - (reference type)
x = [1,2,3]
y = x
y.append(4)
print(x)
print(y)

# type-safe değildir.
number = 5
number = "Halit"
print(number)

# index 
names = ["Halit", "Esra", "Lütfiye", 5, True]
print(names[0]) #ilk değer
print(names[-1]) #son değer
print(names[0:2]) # dilimleme, slicing
print(names[:2])
print(names[0:0:2])
print(names[::2])
print(names[1:])

numbers = [0,10,24,12,56, 5,5]
print(len(numbers)) # length
numbers.sort(reverse=False) # default => false küçükten büyüğe. True => Büyükten küçüğe
print("***")
print((numbers)) # sıralamak
print(numbers.count(110)) # belirli bir değerin tekrar sayısına ulaşmak.
numbers.reverse()
print(numbers)

# döngüler
# yazdığım x satır kodun y adet çalışmasını sağlamak

# indentation mantığı
# for { } - (scope)
my_variable2 = "For disindaki değişken"

for i in range(5):
    my_variable = "For içindeki değişken"
    print(my_variable2)
    print(i)
    print("For çalisti")

print(my_variable)

for i in range(5,10):
    print(i)
print("**********")
for i in range(5,10,2):
    print(i)

#range(başlangıç (0),bitiş,adım (1))
#range(bitiş) => tek zorunlu

# tab -> 1 indent sağa
# shift + tab -> 1 indent sola

#
students = ["Merve","Şeyda","Şüheda","Ece"]

for student in students:
    print(student)


# koşul - şart blokları
# bir duruma göre belirli kod bloklarını çalıştırmak
note = 50
# bir if bloğu sadece bir sonuç çalıştırır.
if note >= 50:
    print("Geçtiniz")

if note == 50:
    print("Sınırdan geçtiniz.")
else:
    print("Kaldınız")
#