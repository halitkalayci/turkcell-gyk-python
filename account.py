class Account:
    def __init__(self,startBalance):
        self._balance = startBalance
    def deposit(self, amount):
        self._balance += amount
        print(f"{amount} kadar para yatırılıyor.")
    def withdraw(self, amount):
        if(self._balance < amount):
            print("Bu kadar miktar çekemezsiniz..")
            return
        self._balance -= amount
        print(f"{amount} kadar para çekiliyor..")
    def print_status(self):
        print(f"Hesap bakiyesi: {self._balance}")