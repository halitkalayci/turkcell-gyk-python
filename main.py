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
