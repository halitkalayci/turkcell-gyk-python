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