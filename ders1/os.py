gun = int(input("Gun daxil edin"))
saat = int(input("Saaati daxil edin"))
deqiqe = int(input("Deqiqeni daxil edin"))
saniye = int(input("Saniyeyi daxil edin"))

total_saniye = (gun * 24 * 60 * 60) + (saat * 60 * 60) + (deqiqe * 60) + saniye

print(total_saniye)
