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
        self.x() # -> self -> classın kendisi
        #super.__call__() # -> super -> kalıtım aldığım classı
        print("Bird sound")

# Cat -> Animal,Mammal        
class Cat(Animal):
    def make_sound(self): 
        print("Cat sound")

b1 = Bird("Bird")
b1.make_sound()

c1 = Cat("Cat")
c1.make_sound()
#