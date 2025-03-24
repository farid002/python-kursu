"""
Heyvan adlı əsas sinif yaradın (parent class):

ad, yaş, cins (dişi, erkək) atributunu təyin edin.

ses_cixar() adlı metod yaradın və bu metod "Bu heyvan səs çıxarır" mesajını qaytarmalıdır.


İki fərqli törəmə sinif (child classes) yaradın:

İt adlı sinif yaradın və ses_cixar() metodunu “Hav-hav!” qaytaracaq şəkildə yenidən yazın.
Pişik adlı sinif yaradın və ses_cixar() metodunu “Miyov-miyov!” qaytaracaq şəkildə yenidən yazın.

Test edin:
It və Pişik siniflərindən bir neçə obyekt yaradın və onların ses_cixar() metodunu çağıraraq fərqi göstərin.
"""


class Heyvan:
    def __init__(self, ad, yas, cins):
        self.ad = ad
        self.yas = yas
        self.cins = cins


    def ses_cixar(self):
        return "Bu heyvan səs çıxarır"

class It(Heyvan):
    def ses_cixar(self):
        return  "Hav-hav!"

class Pisik(Heyvan):
    def ses_cixar(self):
        return "Miav!"




# test

it1 = It("Bobik", 3, "Erkək")
pisik1 = Pisik("Nuna", 4, "Dişi")
heyvan1 = Heyvan("Generic Animal", 2, "Dişi")


print(it1.ses_cixar())
print(pisik1.ses_cixar())
print(heyvan1.ses_cixar())
