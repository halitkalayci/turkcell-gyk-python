print("oop")

class Car:
    name = "" #property-özellik (attribute-field)
    def start(self):
        print(f"{self.name} isimli araç başlatılıyor.")
    def stop(self): #(this) self -> classın kendisini ifade eder.
        print("Araç durduruluyor.")

c1 = Car() # yeni instance oluşturma c1->instance (örnek)
c1.name = "Hyundai"
c1.start()
c1.stop()

c2 = Car()
c2.name = "Honda"
c2.start()