"""
Istifadəçidən istifadəçi adı və şifrə alın. Yazacağınız kod istifadəçinin və yoxlayıb müxtəlif şərtlər və mesajlar göstərməlidir. Tapşırıq həm , həm də strukturlarını və əhatə edir.Şərtlər:


Əgər adın uzunluğu 3 simvoldan qısadırsa, "Ad çox qısadır." mesajını göstərin.
Əgər adın uzunluğu 15 simvoldan uzundursa, "Ad çox uzundur." mesajını göstərin.
Əks halda, "Ad qəbul edildi." yazdırın.

Şifrə ən azı 8 simvol olmalıdır. Əgər deyilirsə, "Şifrə çox qısadır." mesajını göstərin.
Əgər şifrə tamamilə rəqəmlərdən ibarətdirsə, "Şifrə tam rəqəm ola bilməz." mesajını yazdırın.
Şifrənin ilk hərfi böyük hərf olmalıdır. Əgər deyilirsə, "Şifrənin ilk hərfi böyük olmalıdır." yazdırın.
Şifrənin sonunda "!" işarəsi olmalıdır. Əgər deyilirsə, "Şifrə '!' ilə bitməlidir." mesajını göstərin.
Əgər şifrə bütün şərtləri ödəyirsə, "Şifrə qəbul edildi." yazdırın.
Əgər adın ilk üç hərfi şifrədə varsa, "Adın bir hissəsi şifrədə istifadə olunmamalıdır." yazdırın.
"Qeydiyyat uğurla tamamlandı!" yazdırın.

"""

name = str(input("Adi daxil edin: "))


if len(str(name)) <= 3:
    print("Ad çox qısadır.")
elif len(str(name)) > 15:
    print("Ad çox uzundur.")
else:
    print("Ad qəbul edildi.")

print(" ")

pwd = input("Shifre daxil edin: ")


if len(pwd) < 8:
    print("Şifrə çox qısadır.")
    if pwd.isdigit() == True:
        print("Şifrə tam rəqəm ola bilməz.")
    if pwd.capitalize() == False:
        print("Şifrənin ilk hərfi böyük olmalıdır.")
else:
    print("Qeydiyyat uğurla tamamlandı!.")


