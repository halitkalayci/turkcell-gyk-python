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
number = 5 #int
number = "Halit" #string
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

for student in students:
    if student == "Şüheda":
        break # bu loopu burda bitir
    print(student)
else:
    print("1. For loopu bitti.")
print("******")

for student in students:
    if student == "Şüheda":
        continue # bu iterasyonu burda bitir.
    print(student)
else: # break ile kırılmadıysa loop bitiminde çalışır.
    print("2. For loopu bitti.")


# while döngüsü
i=0
while i<5: # koşul sağlandığı sürece buradaki döngüyü çalıştır.
    print(i)
    i += 1

student_name = "Halit"

#while student_name == "Halit":
#    print("**")

# match-case 3.9,3.8
print("************** DERS 2 ********************")
# string
age = 25 # dışarıdan int olarak geliyor
name = "Halit"
# text = "Merhaba, adım " + name + " yaşım " + age # formatlama # hatalı

#built-in

text = f"Merhaba, adım {name} yaşım {15+15}" # f-string
#text = "Merhaba, adım {} yaşım {}".format(name, age)
#text = "Merhaba, adım {name} yaşım {age}".format(name=name, age=age)
print(text)

text2 = "tURKcell kodlamaio"
print(text2.capitalize())
print(text2.lower())
print(text2.upper())
print(text2.endswith("oio")) # case-sensitive
print(text2.startswith("tu")) # case-sensitive
print(text2.lower().startswith("turkc"))

age2 = "25"
print(age2.isalnum())
print(age2.isnumeric())
print(age2.isascii())
print(age2.isspace())

text3 = 'Merhaba Turkcell'
print(text3)

long_text = '''Satır 1
Satır 2
Satır 3''' # 3 tırnak ile çoklu satır metinsel ifade oluşturulabilir.

print(long_text)

escape_characters = "Bugünkü konumuz \"Python ile programlama\"" #escape character \
print(escape_characters)

escape_characters2 = "Bugünkü konumuz \n \\ Python ile Programlama"
print(escape_characters2)

folder_path = r"C:\Program Files\Turkcell\n" #raw -> kaçış karakterlerini iptal et.
print(folder_path)

# functions
print("X Fonksiyonu çalıştı..")
print("X Fonksiyonu çalıştı..")
print("X Fonksiyonu çalıştı..")
print("X Fonksiyonu çalıştı..")
print("X Fonksiyonu çalıştı..")
print("X Fonksiyonu çalıştı..")
print("X Fonksiyonu çalıştı..")
print("X Fonksiyonu çalıştı..")
print("X Fonksiyonu çalıştı..")
print("X Fonksiyonu çalıştı..")

# define-definition
def say_hello():
    print("Merhaba Turkcell")

say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()

# parametre, argüman* args
def calculate_age(year):
    age = 2025 - year
    print(f"Hesaplanan yaşınız {age}")

calculate_age(1998)
calculate_age(1985)
calculate_age(2000)
calculate_age(2002)
calculate_age(1978)

def say_hi(fname, lname):
    print(f"Merhaba {fname} {lname}")

say_hi("Halit Enes","Kalayci")


def calculate_return_age(year):
    age = 2025 - year
    return age

age5 = calculate_return_age(2000)
print(age5)
if(age5 < 18):
    print("Reşit değil")
else:
    print("Reşit")

# *args
def print_lessons(*lessons):
    for lesson in lessons:
        print(lesson)
print_lessons("Java","Python")
print_lessons("C#")
print_lessons("İstatistik","Matematik","Biyoloji")
#

# **kwargs -> keyword args
def introduce_instructor(**instructor):
    print(f"Ad: {instructor['fname']}  Soyad: {instructor['lname']} Yaş: {instructor['age']}")

introduce_instructor(fname="Halit Enes",lname="Kalaycı",age=25)
introduce_instructor(fname="Engin",lname="Demiroğ",age=25)


def default_parameter(name, country = "Turkey", city="Istanbul"):
    print(f"{name} {country} {city}")

default_parameter(name="A", city="Atina")
default_parameter("B","Bulgaria")
default_parameter("C")


#def default_parameter2(name = "Halit",country):
    #print(f"{name} {country}")

#default_parameter2("A","Greece")
#default_parameter2("B","Bulgaria")
#default_parameter2("","C")

#oop

#20:30 -> 

# oop - nesne yönelimli programlama