"""
  BankHesabi adlı bir sinif yaradın. Bu sinifdə müştərinin adı, email adresi, hesab nömrəsi və balansı saxlanmalıdır. Hesaba pul yatırmaq, çıxarmaq və balans yoxlamaq üçün metodlar yaradın.

  Tapşırıq:

   - BankHesabi sinifini yaradın və ad, email adresi, hesab_nomresi, balans atributlarını əlavə edin.
   - pul_yatir metodunu yaradın ki, müştəri hesabına müəyyən bir məbləğ yatırsın və balans artsın.
   - pul_cixar metodunu yaradın ki, müştəri hesabından müəyyən bir məbləğ çıxarsın və balans azalsın.
   - balans_goster metodunu yaradın ki, müştərinin cari balansını ekrana çap etsin.
   - tam_melumat metodu yaradın ki, müştərinin bütün məlumatlarını ekrana çap etsin
"""
"""
  Daha öncə yazdığınız kodu genişləndirirərək,
  İstifadəçiyə sonsuz menyu göstərin və bir əməliyyat etməsi üçün hərf daxil etməsini istəyin:

  - i: Məlumatları gör (bütün məlumatları versin)
  - +: Balansı artır (istifadəçi yazdığı məbləğ qədər balansı artırsın)
  - -: Pul çıxartmaq (istifadəçi yazdığı məbləğ qədər balansı azaltsın)
  - b: Balansı göstər
  - x: Çıxış:
"""
class BankHesabi:
    def __init__(self, ad, email, hesab_nomresi, balans = 0):
        self.ad = ad
        self.email = email
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def pul_yatir(self, mebleg):
        if mebleg > 0:
            self.balans += mebleg
            print(f"{mebleg} AZN hesaba yatirildi. Yeni Balans: {self.balans} AZN")

    def pul_cixar(self, mebleg):
         if 0 < mebleg <= self.balans:
            self.balans -= mebleg
            print(f"{mebleg} AZN hesabdan cixarildi. Yeni Balans: {self.balans} AZN")

    def balans_goster(self):
        print(f"{self.ad} ücün cari balans: {self.balans} AZN ")

    def tam_melumat(self):
        print(f"Ad: {self.ad}, \nEmail: {self.email} \nHesab: {self.hesab_nomresi} \nBalans: {str(self.balans)} AZN")

hesab = BankHesabi("Osman Osmanov", "osman@gmail.com", "123456789101")
hesab.pul_yatir(500)
hesab.pul_cixar(200)
hesab.balans_goster()
hesab.tam_melumat()

while True:
    print("\n=== Bank Menü ===")
    print("i: Melumat gör")
    print("+ : Balansi artir")
    print("- : Pul cixartmaq")
    print("b : Balansı göstər")
    print("x : Çıxış")

    secim = input("Secim edin:").strip().lower()

    if secim == "i":
        hesab.tam_melumat()
    elif secim == "+":
        mebleg = int(input("Ytirmaq istetiyiniz meblegi daxik edin"))
        hesab.pul_yatir(mebleg)
    elif secim == "-":
        mebleg = int(input("Cixarmaq istetiyiniz meblegi daxik edin"))
        hesab.pul_cixar(mebleg)
    elif secim == "b":
        hesab.balans_goster()
    elif secim == "x":
        print("Cixis edildi.")
        break
    else:
        print("Yalnis secim, yeniden cehd edin.")