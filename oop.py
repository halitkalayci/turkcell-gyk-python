print("oop")

class Car:
    # name = "" #property-özellik (attribute-field)
    def __init__(self,name,model, year=None): # bir classın yapıcı bloğu-constructor
        self.name = name
        self.model = model
        self.year = year
        print("İnit çalıştı")
        
    def start(self, x, y):
        print(f"{self.name} {self.model} {self.year} isimli araç başlatılıyor. {x} {y}")

    def stop(self): #(this) self -> classın kendisini ifade eder.
        print("Araç durduruluyor.")

c1 = Car("Hyundai","i20") # yeni instance oluşturma c1->instance (örnek)
c1.start(1,2)
c1.stop()

c2 = Car("Honda","Civic") #yapıcı blok
c2.start(2,3)


# oop concepts

#kalıtım-inheritance

class Animal(): #super-class
    def __init__(self,name):
        self.name = name
    def make_sound(self):
        print("Animal sound")
    def x(self):
        print("Animal X Methodu")

#class Mammal(Animal):
 #   pass
# Cat -> Mammal -> Animal

class Bird(Animal): #sub-class
    def make_sound(self): # Method Overriding - Method Ezme
        print("Bird sound") # make_sound()
        super().make_sound() # super classında make_sound()

# Cat -> Animal,Mammal        
class Cat(Animal):
    def make_sound(self): 
        print("Cat sound")

b1 = Bird("Bird")
b1.make_sound()

c1 = Cat("Cat")
c1.make_sound()
#

# nesne koleksiyonundaki nesnelerin aynı davranışı farklı şekillerde yapmasıdır.
animals = [Cat("Cat2"), Bird("Bird2")]
print("*****")
for animal in animals:
    animal.make_sound() #polymorphism - çok biçimlilik
print("*****")

#
#

#Encapsulation-Kapsülleme -> Fieldlara dışardan erişimi kapatıp bu fieldların methodlar ile yönetilmesini sağlamak.
class Account:
    def __init__(self,startBalance):
        self.__balance = startBalance #private
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} kadar para yatırılıyor.")
    def withdraw(self, amount):
        if(self.__balance < amount):
            print("Bu kadar miktar çekemezsiniz..")
            return
        self.__balance -= amount
        print(f"{amount} kadar para çekiliyor..")
    def print_status(self):
        print(f"Hesap bakiyesi: {self.__balance}")
    def get_balance(self):
        return self.__balance
#    def set_balance(self,balance):
#        self.__balance = balance

class Acc(Account):
    def deposit(self, amount, x):
        self.__balance += amount
        print(f"{amount} kadar para yatırılıyor. {x}")
    def a(self):
        self.__balance += 500
        print(self.__balance)
#

a1 = Account(1000)
#a1.__balance -= 5000
a1.get_balance()
a1.deposit(500)
a1.withdraw(1200)
a1.withdraw(1200)
a1.print_status()

a2 = Acc(500)
a2.deposit(5000, 1)
#a2.deposit(5000)
a2.a()

# Loglama BaseLogger -> log() -> DB'e yaz.
# 3 tane logger -> XLogger, YLogger, ZLogger log() override et, not defterine yaz.

