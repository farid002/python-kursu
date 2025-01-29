"""
İstifadəçidən müddəti gün, saat, dəqiqə və saniyə kimi oxuyan skript yazın.
Bu müddətlə bərabər olan ümumi saniyə sayını hesablayın və terminalda göstərin.
"""
daxil_saniye=int(input("saniye daxil edin\n"))
daxil_deqiqe=int(input("deqiqe daxil edin\n"))
daxil_saat=int(input("saat daxil edin\n"))
daxil_gun=int(input("gun daxil edin\n"))

print(f"Sizin muddetiniz saniye ile: {(daxil_gun*86400)+(daxil_saat*3600)+(daxil_deqiqe*60)+(daxil_saniye)}")