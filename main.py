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