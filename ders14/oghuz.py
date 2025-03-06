"""
  BankHesabi adlı bir sinif yaradın. Bu sinifdə müştərinin adı, email adresi, hesab nömrəsi və balansı saxlanmalıdır.
   Hesaba pul yatırmaq, çıxarmaq və balans yoxlamaq üçün metodlar yaradın.

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
  - x: Çıxış
"""

class BankHesabi:

    def __init__(self, name, email, hesab_nomresi, balans):
        self.name = name
        self.email = email
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def balans_artim(self, artacaq_mebleg):
        self.balans = self.balans + artacaq_mebleg

    def balans_azalt(self, azalacaq_mebleg):
        self.balans = self.balans - azalacaq_mebleg

    def balans_goster(self):
        print(self.balans)

    def tam_melumat(self):
        print(f"Adiniz:{self.name}\nEmail:{self.email}\nHesab_nomresi:{self.hesab_nomresi}\nBalansiniz:{self.balans}")


if __name__ == "__main__":
    oghuzun_hesabi = BankHesabi("Oghuz", "omedineli@gmail.com", 123456, 100)
    while True:
        a = input("i: Məlumatları gör, +: Balansı artır, -: Pul çıxartmaq, b: Balansı göstər, x: Çıxış\n")
        if a == "+":
            oghuzun_hesabi.balans_artim(int(input("Deyer daxil edin")))
            oghuzun_hesabi.balans_goster()
        if a == "i":
            oghuzun_hesabi.tam_melumat()
        if a == "-":
            oghuzun_hesabi.balans_azalt(int(input("Deyer daxil edin")))
            oghuzun_hesabi.balans_goster()
        if a == "b":
            oghuzun_hesabi.balans_goster()
        if a == "x":
            break