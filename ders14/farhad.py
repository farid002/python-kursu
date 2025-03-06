class BankAccount:
    def __init__(self, name, email, account_number, balance):
        self.name = name
        self.email = email
        self.account_number = account_number
        self.balance = balance

    def pul_yatir(self, amount):
        self.balance += amount
        hesab.balans_goster()

    def pul_cixar(self, amount):
        self.balance -= amount
        hesab.balans_goster()


    def balans_goster(self):
        print(self.balance)

    def tam_melumat(self):
        print(f"Ad: {self.name}")
        print(f"Email: {self.email}")
        print(f"Hesab Nömresi: {self.account_number}")
        print(f"Balans: {self.balance} AZN.")

hesab = BankAccount("Farhad Valiyev", "email@mail.com", "DE123456", 1000)

print("\nMenyu:")
print("i: Məlumatları gör")
print("+: Balansı artır")
print("-: Pul çıxartmaq")
print("b: Balansı göstər")
print("x: Çıxış")
print("\n")
while True:
    user_input = input("bir əməliyyat etməsi üçün hərf daxil edin: ")
    if user_input == "i":
        hesab.tam_melumat()
    elif user_input == "+":
        amount = int(input("Balansı artır: "))
        hesab.pul_yatir(amount)
    elif user_input == "-":
        amount = int(input("Pul çıxartmaq: "))
        hesab.pul_cixar(amount)
    elif user_input == "b":
        hesab.balans_goster()
    elif user_input == "x":
        print("Çıxış etdiniz")
        break
    else:
        print("Yalnis melumatlardir.Zehmet olmasa yeniden daxil edin!")